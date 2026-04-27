# 🧩 1️⃣ Named Entity Recognition (NER) App

# Start simple using spaCy

# 📌 What it does

# Extracts:

# Names (PERSON)
# Places (GPE)
# Organizations (ORG)

import streamlit as st
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition (NER) App")

user_input = st.text_area("Enter some text to analyze for named entities:")

if user_input:
    doc = nlp(user_input)
    st.write("Named Entities Found:")
    for ent in doc.ents:
        st.write(f"{ent.text} ({ent.label_})")


# 💡 Example Input
# Elon Musk founded SpaceX in the USA

# 👉 Output:

# Elon Musk → PERSON
# SpaceX → ORG
# USA → GPE