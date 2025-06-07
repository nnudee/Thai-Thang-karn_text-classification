import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt
import numpy as np

# 🔧 เปลี่ยนชื่อโมเดลให้เป็นของคุณ (จาก Hugging Face repo)
MODEL_NAME = "nnudee/Thai-Thangkarn-classifier"

# โหลด tokenizer และ model
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()
model.eval()

# UI Streamlit
st.title("🧠 Text Classifier พร้อมกราฟเปอร์เซ็นต์")

user_input = st.text_area("🔍 ใส่ข้อความที่ต้องการให้โมเดลทำนาย", "")

if user_input:
    # เข้ารหัสข้อความ
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits[0]
    probs = torch.nn.functional.softmax(logits, dim=-1).numpy()

    # ดึง label name ถ้ามี
    if model.config.id2label:
        labels = [model.config.id2label[i] for i in range(len(probs))]
    else:
        labels = [f"Class {i}" for i in range(len(probs))]

    # แสดงผลลัพธ์ทีละบรรทัด
    st.subheader("ผลการทำนาย (เป็นเปอร์เซ็นต์)")
    for label, prob in zip(labels, probs):
        st.write(f"**{label}**: {prob * 100:.2f}%")

    # กราฟแท่ง
    st.subheader("📊 กราฟความน่าจะเป็นของแต่ละคลาส")
    fig, ax = plt.subplots()
    ax.barh(labels, probs * 100)
    ax.set_xlabel("Probability (%)")
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    st.pyplot(fig)
