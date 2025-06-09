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
    st.subheader("แสดงเป็นแท่งเดียวแบบแบ่งตามเปอร์เซ็นต์")

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

    # จัดข้อมูลสำหรับกราฟ
    sorted_indices = np.argsort(probs)[::-1]
    sorted_labels = [labels[i] for i in sorted_indices]
    sorted_probs = [probs[i] for i in sorted_indices]
    colors = ['gray'] * len(sorted_probs)
    colors[0] = 'green'

    left = 0
    for i in range(len(sorted_probs)):
        ax.barh(0, sorted_probs[i], left=left, height=0.4, color=colors[i], edgecolor='white')
        ax.text(
            left + sorted_probs[i]/2, 0,
            f"{sorted_labels[i]} ({sorted_probs[i]*100:.1f}%)",
            va='center', ha='center', color='white', fontsize=10,
            fontproperties=font_use  # ใช้ฟอนต์ Sarabun ถ้ามี
        )
        left += sorted_probs[i]

    ax.set_xlim(0, 1)
    ax.axis('off')
    st.pyplot(fig)
