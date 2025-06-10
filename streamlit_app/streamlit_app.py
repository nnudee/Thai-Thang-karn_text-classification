import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
import pandas as pd

MODEL_NAME = "nnudee/Thai-Thangkarn-classifier"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()
model.eval()

st.title("ประโยคของคุณทางการระดับไหน?")

# ✅ โหลด test set
@st.cache_data
def load_test_data():
    csv_path = os.path.join(os.path.dirname(__file__), "test_data.csv")
    df = pd.read_csv(csv_path)
    return df["output"].tolist()


test_texts = load_test_data()

# ✅ ให้ผู้ใช้เลือกข้อความจาก test set
selected_text = st.selectbox("เลือกข้อความจากชุดทดสอบ", test_texts)

# ✅ ช่องแสดงข้อความที่เลือก (แก้ไขได้)
user_input = st.text_area("สามารถแก้ไขข้อความก่อนทำนายได้", value=selected_text)

# ✅ ประมวลผลด้วยโมเดล
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

    # ✅ โหลดฟอนต์ Sarabun
    font_path = os.path.join(os.path.dirname(__file__), "Sarabun-2", "Sarabun-Regular.ttf")
    if os.path.exists(font_path):
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
        font_use = font_prop
    else:
        st.warning("⚠️ ไม่พบฟอนต์ Sarabun ใช้ฟอนต์ระบบแทน")
        font_use = None

    # ✅ แสดงผลลัพธ์ทีละบรรทัด
    st.subheader("ผลการทำนาย (เป็นเปอร์เซ็นต์)")
    for label, prob in zip(labels, probs):
        st.write(f"**{label}**: {prob * 100:.2f}%")

    # ✅ กราฟหลายแท่ง
    st.subheader("แสดงเปอร์เซ็นต์แยกตามระดับความสุภาพ")
    fig, ax = plt.subplots(figsize=(8, 4))

    bars = ax.bar(labels, probs, color=["green" if i == np.argmax(probs) else "gray" for i in range(len(probs))])
    for bar, prob in zip(bars, probs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{prob*100:.1f}%",
                ha='center', va='bottom', fontsize=10, fontproperties=font_use if font_use else None)

    ax.set_ylim(0, 1)
    ax.set_ylabel("สัดส่วน (0 - 1)", fontproperties=font_use if font_use else None)
    ax.set_title("ความมั่นใจของโมเดลในแต่ละระดับ", fontproperties=font_use if font_use else None)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontproperties=font_use if font_use else None, fontsize=10)

    st.pyplot(fig)
