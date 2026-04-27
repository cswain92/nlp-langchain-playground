# Chatbot using Transformers
# Use Hugging Face Transformers
from transformers import pipeline
import streamlit as st


st.title("AI Chatbot using Transformers")

chatboat = pipeline("text-generation", model="gpt2")

user_input = st.text_area("Enter your message to the chatbot:")

if user_input:
    responce = chatboat(user_input, max_length=100)
    st.write("Chatbot Response:", responce[0]['generated_text'])