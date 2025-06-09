import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

MODEL_NAME = "nnudee/Thai-Thangkarn-classifier"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()
model.eval()

st.title("ประโยคของคุณทางการระดับไหน?")

user_input = st.text_area("ใส่ข้อความที่ต้องการทำนาย", "")

if user_input:
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits[0]
    probs = torch.nn.functional.softmax(logits, dim=-1).numpy()

    if model.config.id2label:
        labels = [model.config.id2label[i] for i in range(len(probs))]
    else:
        labels = [f"Class {i}" for i in range(len(probs))]

    # แสดงผลลัพธ์ทีละบรรทัด
    st.subheader("ผลการทำนาย (เป็นเปอร์เซ็นต์)")
    for label, prob in zip(labels, probs):
        st.write(f"**{label}**: {prob * 100:.2f}%")

    # ==== แสดงกราฟ ====

    fig, ax = plt.subplots(figsize=(6, 1))

    # โหลดฟอนต์ Sarabun (โดยใช้ path แบบปลอดภัย)
    font_path = os.path.join(os.path.dirname(__file__), "Sarabun-2", "Sarabun-Regular.ttf")
    if os.path.exists(font_path):
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
        font_use = font_prop
    else:
        st.warning("⚠️ ไม่พบฟอนต์ Sarabun ใช้ฟอนต์ระบบแทน")
        font_use = None


    # ==== แสดงกราฟแบบแท่งหลายแท่ง ====
    st.subheader("แสดงเปอร์เซ็นต์แยกตามระดับความสุภาพ")

    fig, ax = plt.subplots(figsize=(8, 4))

    bars = ax.bar(labels, probs, color=["green" if i == np.argmax(probs) else "gray" for i in range(len(probs))])

    # เพิ่มตัวเลขบนแต่ละแท่ง
    for bar, prob in zip(bars, probs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{prob*100:.1f}%", 
                ha='center', va='bottom', fontsize=10, fontproperties=font_use if font_use else None)

    ax.set_ylim(0, 1)
    ax.set_ylabel("สัดส่วน (0 - 1)")
    ax.set_title("ความมั่นใจของโมเดลในแต่ละระดับ", fontproperties=font_use if font_use else None)

    # ตั้งชื่อแกนด้วยฟอนต์ไทย
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontproperties=font_use if font_use else None, fontsize=10)

    st.pyplot(fig)