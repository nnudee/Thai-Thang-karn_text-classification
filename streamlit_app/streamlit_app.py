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
