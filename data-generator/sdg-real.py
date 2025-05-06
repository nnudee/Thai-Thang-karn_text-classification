import argparse
import random
import re
import csv
import time
from typing import List, Tuple
import sdg_config  # คอนฟิก labels/use_case/prompt examples
import os
from openai import OpenAI

# สร้าง client Typhoon (OpenAI-compatible)
client = OpenAI(
    api_key=os.environ.get("TYPHOON_API_KEY", ""),
    base_url="https://api.opentyphoon.ai/v1"
)
model_name = "typhoon-v2-70b-instruct"


def parse_string(input_string: str) -> Tuple[str, str]:
    output_match = re.search(r"OUTPUT:(.*?)(REASONING:|$)", input_string, re.DOTALL)
    reasoning_match = re.search(r"REASONING:(.*)$", input_string, re.DOTALL)
    output = output_match.group(1).strip() if output_match else ""
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""
    return output, reasoning


def generate_from_typhoon(prompt: str, system_prompt: str = "") -> str:
    try:
        res = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"OUTPUT: [ERROR] REASONING: {str(e)}"


def sdg(sample_size: int,
        labels: List[str],
        label_descriptions: str,
        categories_types: List[str],
        use_case: str,
        prompt_examples: str,
        batch_size: int = 10,
        output_file: str = "generated_data.csv",
        system_prompt_path: str = "system_prompt.txt") -> None:

    if os.path.exists(system_prompt_path):
        with open(system_prompt_path, "r", encoding="utf-8") as f:
            system_prompt = f.read().strip()
    else:
        system_prompt = ""  # ใช้ empty system prompt ถ้าไม่มีไฟล์

    total_combinations = len(labels) * len(categories_types)
    samples_per_combination = sample_size // total_combinations

    with open(output_file, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["text", "label", "category", "reasoning"])

        for label in labels:
            for category in categories_types:
                for batch_start in range(0, samples_per_combination, batch_size):
                    rows = []
                    for _ in range(min(batch_size, samples_per_combination - batch_start)):
                        prompt = f"""
{prompt_examples}

Given the use-case: {use_case}
Category: {category}
Label: {label} ({label_descriptions.get(label, '')})

Generate a synthetic example:
OUTPUT:
REASONING:
"""
                        result = generate_from_typhoon(prompt, system_prompt)
                        output, reasoning = parse_string(result)
                        rows.append([output, label, category, reasoning])

                    writer.writerows(rows)
                    print(f"Saved batch: {label} - {category} ({batch_start + len(rows)} / {samples_per_combination})")
                    time.sleep(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample_size", type=int, default=50)
    parser.add_argument("--batch_size", type=int, default=10)
    parser.add_argument("--output_file", type=str, default="generated_data.csv")
    parser.add_argument("--system_prompt_path", type=str, default="system_prompt.txt")
    args = parser.parse_args()

    sdg(
        sample_size=args.sample_size,
        labels=sdg_config.labels,
        label_descriptions=sdg_config.label_descriptions,
        categories_types=sdg_config.categories_types,
        use_case=sdg_config.use_case,
        prompt_examples=sdg_config.prompt_examples,
        batch_size=args.batch_size,
        output_file=args.output_file,
        system_prompt_path=args.system_prompt_path
    )


if __name__ == "__main__":
    main()
