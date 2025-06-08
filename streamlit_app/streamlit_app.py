import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt
import numpy as np

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

    # วาดกราฟแท่งแนวนอน (horizontal bar) แบบ stacked ในแท่งเดียว
    st.subheader("แสดงเป็นแท่งเดียวแบบแบ่งตามเปอร์เซ็นต์")

    fig, ax = plt.subplots(figsize=(8, 1.5))

    # จัดเรียง label ตามลำดับของ prob (ไม่จำเป็นต้องเรียงถ้าไม่อยาก)
    sorted_indices = np.argsort(probs)[::-1]
    sorted_labels = [labels[i] for i in sorted_indices]
    sorted_probs = [probs[i] for i in sorted_indices]

    # กำหนดสี โดย label ที่มีเปอร์เซ็นต์มากที่สุดเป็นสีเขียว
    colors = ['gray'] * len(sorted_probs)
    colors[0] = 'green'  # สีของ label ที่ความน่าจะเป็นมากที่สุด

    left = 0
    for i in range(len(sorted_probs)):
        ax.barh(0, sorted_probs[i], left=left, height=0.5, color=colors[i], edgecolor='white')
        ax.text(left + sorted_probs[i]/2, 0, f"{sorted_labels[i]} ({sorted_probs[i]*100:.1f}%)", 
                va='center', ha='center', color='white', fontsize=9)
        left += sorted_probs[i]

    ax.set_xlim(0, 1)
    ax.axis('off')  # ซ่อนแกน
    st.pyplot(fig)
