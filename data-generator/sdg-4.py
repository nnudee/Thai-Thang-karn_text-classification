import random
import pandas as pd
import sdg_config_flat_prompt as config

def build_prompts(samples_per_combination: int = 100):
    prompts = []
    for label in config.labels:
        for contact in config.contact_chanel:
            for category, types in config.categories_types.items():
                for t in types:
                    for _ in range(samples_per_combination):
                        # สุ่ม template ตัวอย่างตามระดับความสุภาพ
                        prompt_template = random.choice(config.prompt_examples.get(label, [""]))
                        # สุ่มคำสรรพนามตาม label
                        pronoun = random.choice(config.pronouns_by_level.get(label, [""]))

                        # สร้าง OUTPUT โดยแทนที่ placeholder
                        output = prompt_template.replace("{pronoun}", pronoun).replace("{type}", t).replace("{contact}", contact)

                        # สร้าง REASONING อิงตาม label และ context
                        reasoning = f"ข้อความนี้สะท้อนระดับ '{label}' ด้วยการเลือกใช้คำ เช่น '{pronoun}' และการเขียนแบบเหมาะสมกับช่องทาง {contact} และบริบท {category} ({t})"

                        # เพิ่มลงใน list
                        prompts.append({
                            "LABEL": label,
                            "CONTACT": contact,
                            "CATEGORY": category,
                            "TYPE": t,
                            "OUTPUT": output.strip(),
                            "REASONING": reasoning.strip()
                        })
    return pd.DataFrame(prompts)

