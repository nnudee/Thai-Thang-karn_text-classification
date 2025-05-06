import os
import random
import re
import time
import requests
import pandas as pd
from datetime import datetime
from huggingface_hub import login

# อ่าน token จากไฟล์ token.txt
with open("token.txt", "r") as f:
    token = f.read().strip()

login(token)

headers = {"Authorization": f"Bearer {token}"}

def parse_string(input_string: str):
    match = re.search(r"OUTPUT:\s*(.+?)\s*REASONING:\s*(.+)", input_string, re.DOTALL)
    if not match:
        raise ValueError("The generated response is not in the expected format.")
    return match.group(1).strip(), match.group(2).strip()

def call_api(prompt, model, max_retry=3, wait_time=5):
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs": prompt}

    for attempt in range(max_retry):
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            result = response.json()
            return result[0]["generated_text"]

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}/{max_retry} failed: {e}")
            if attempt < max_retry - 1:
                time.sleep(wait_time)
            else:
                raise Exception(f"Failed after {max_retry} attempts: {e}")

def sdg(
    labels,
    label_descriptions,
    contact_chanel,
    categories_types,
    use_case,
    prompt_examples,
    model,
    max_new_tokens,
    batch_size,
    output_dir,
    save_reasoning
):
    samples_per_combination = 20
    all_entries = []

    # สร้างทุก combination ของ label + contact + category + type
    for label in labels:
        for contact in contact_chanel:
            for category, types in categories_types.items():
                for type_ in types:
                    for _ in range(samples_per_combination):
                        all_entries.append({
                            "label": label,
                            "contact": contact,
                            "category": category,
                            "type": type_
                        })

    random.shuffle(all_entries)
    sample_size = len(all_entries)
    num_batches = (sample_size + batch_size - 1) // batch_size
    print(f"Total entries to generate: {sample_size} in {num_batches} batch(es)")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{timestamp}.csv")
    os.makedirs(output_dir, exist_ok=True)

    for batch in range(num_batches):
        start = batch * batch_size
        end = min(start + batch_size, sample_size)
        batch_data = []

        for i in range(start, end):
            e = all_entries[i]

            prompt = f"""
You should create synthetic data for specified labels and categories. This is especially useful for conversation between professor and student in Thai language.

*Label Descriptions*
    - พิธีการ: Text have Highly ritualistic, eloquent, grammatically perfect, uses formal expressions strictly. It is typically used in Thai Royal ceremonies, national events, parliamentary sessions, formal speeches, graduation. Politeness level is 100 percentage.
    - ทางการ: Text have Precise, concise, technical or academic vocabulary, correct grammar. It is typically used in Official announcements, academic papers, government documents, business letters, meetings. Politeness level is 75 percentage..
    - กึ่งทางการ: Text have Similar to official level but more relaxed, simpler sentences, commonly used vocabulary. It is typically used in Group discussions, classroom lectures, informal speeches, news articles, general writing. Politeness level is 50 percentage.
    - ไม่เป็นทางการ: Text have Common expressions, easy to understand, sometimes includes group-specific terms or slang. It is typically used in Casual discussions, entertainment programs, headlines, general publications. Politeness level is 25 percentage.
    - กันเอง: Text have includes slang, regional dialects, vulgar terms; used only in specific groups or contexts. It is typically used in conversations among close friends or family, personal and casual settings. Politeness level is less than 25 percentage.

*Examples*
{prompt_examples}

####################

Generate one output for the classification below.
You may use the examples I have provided as a guide, but you cannot simply modify or rewrite them.
Only return the OUTPUT and REASONING. 
Do not return the LABEL, CATEGORY, or TYPE.

LABEL: พิธีการ
CONTACT: Email
CATEGORY: attendance_issues
TYPE: request leave
OUTPUT:
REASONING:

"""

            try:
                result = call_api(prompt, model)
                text, reasoning = parse_string(result)
            except Exception as ex:
                print(f"Error at sample {i}: {ex}")
                continue

            entry = {
                "text": text,
                "label": e["label"],
                "contact": e["contact"],
                "category": e["category"],
                "type": e["type"],
                "model": model
            }

            if save_reasoning:
                entry["reasoning"] = reasoning

            batch_data.append(entry)

        # Save batch ทันทีหลัง generate เสร็จ
        df = pd.DataFrame(batch_data)
        if batch == 0:
            df.to_csv(output_path, index=False)
        else:
            df.to_csv(output_path, mode='a', header=False, index=False)

        print(f"✅ Saved batch {batch + 1}/{num_batches} to {output_path}")

