import os
import random
import re
from datetime import datetime
import pandas as pd
from transformers import pipeline

def parse_string(input_string: str):
    match = re.search(r"OUTPUT:\s*(.+?)\s*REASONING:\s*(.+)", input_string, re.DOTALL)
    if not match:
        raise ValueError("The generated response is not in the expected format.")
    return match.group(1).strip(), match.group(2).strip()

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

    # ตั้งชื่อไฟล์ผลลัพธ์
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{timestamp}.csv")

    # โหลดโมเดล
    generator = pipeline("text-generation", model=model)

    for batch in range(num_batches):
        start = batch * batch_size
        end = min(start + batch_size, sample_size)
        batch_data = []

        for i in range(start, end):
            e = all_entries[i]

            prompt = f"""You should create synthetic data for specified labels and categories. 
This is especially useful for {use_case}.

*Label Descriptions*
{label_descriptions}

*Examples*
{prompt_examples}

####################

Generate one output for the classification below.
You may use the examples I have provided as a guide, but you cannot simply modify or rewrite them.
Only return the OUTPUT and REASONING. 
Do not return the LABEL, CATEGORY, or TYPE.

LABEL: {e['label']}
CONTACT : {e['contact']}
CATEGORY: {e['category']}
TYPE: {e['type']}
OUTPUT:
REASONING:
"""

            result = generator(prompt, max_new_tokens=max_new_tokens)[0]["generated_text"]

            try:
                text, reasoning = parse_string(result)
            except ValueError:
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

        df = pd.DataFrame(batch_data)
        if batch == 0:
            df.to_csv(output_path, index=False)
        else:
            df.to_csv(output_path, mode='a', header=False, index=False)

        print(f"Saved batch {batch + 1}/{num_batches} to {output_path}")
