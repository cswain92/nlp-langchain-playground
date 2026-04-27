import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader

st.title("NLP Streamlit App - Widgets Showcase")

# 1. Text Input
user_input = st.text_input("Enter some text to analyze:")
if user_input:
    st.write("You entered:", user_input)


# 2. Slider
st.slider("Select a value for analysis", 0, 100, 50)

# 3. Checkbox
if st.checkbox("Show more options"):
    st.write("Here are more options for analysis...")

# 4. Selectbox
option = st.selectbox("Choose an analysis method", ["Sentiment Analysis", "Named Entity Recognition", "Topic Modeling"])
st.write("You selected:", option)

# 5. File Uploader with text, pdf and csv support
uploaded_file = st.file_uploader("Upload a text file (txt, pdf, csv)", type=["txt", "pdf", "csv"])
if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "txt":
        text = uploaded_file.read().decode("utf-8")
        st.write("File content:")
        st.write(text)
    
    elif file_type == "pdf":
        reader = PdfReader(uploaded_file)  # ✅ correct
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        st.write("Extracted PDF content:")
        st.text_area("PDF Content", text, height=300)

    elif file_type == "csv":
        df = pd.read_csv(uploaded_file)
        st.write("CSV content:")
        st.dataframe(df)