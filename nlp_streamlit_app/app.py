
## Create Your First Streamlit App
# import streamlit as st

# st.title("NLP Streamlit App")
# st.write("Welcome to the NLP Streamlit App! This app demonstrates various natural language processing techniques using Streamlit.")


# user_input = st.text_area("Enter some text to analyze:")

# if user_input:
#     st.write("You entered: ", user_input)

## Add Basic NLP (Tokenization)
# import nltk
# nltk.download('punkt_tab')
# from nltk.tokenize import word_tokenize

# if user_input:
#     tokens = word_tokenize(user_input)
#     st.write("Tokens: ", tokens)

## Remove Stopwords
# This code is like a security filter for words. It removes common "filler" words 
# that don't add much meaning, so the computer can focus on the important parts of a sentence.

# from nltk.corpus import stopwords
# nltk.download('stopwords')
# if user_input:
#     stop_words = set(stopwords.words('english'))
#     tokens = word_tokenize(user_input)
#     filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
#     st.write("Filtered Tokens (Stopwords Removed): ", filtered_tokens)


# Add Sentiment Analysis (Simple)
# Option A: Using TextBlob (easy)
# Why?
# The TextBlob.sentiment tool is designed to analyze two things in your text: 

# Polarity: How positive or negative the sentence is (on a scale from -1.0 to 1.0).
# Subjectivity: How much of it is an opinion vs. a factual statement (on a scale from 0.0 to 1.0). 

# Recommended Inputs to Try
# Try these different "vibes" to see how the numbers change:
# Positive Opinion: "I love this movie, it is absolutely amazing!"
# Result: High Polarity (positive), High Subjectivity.
# Negative Opinion: "The service was terrible and the food was cold."
# Result: Low Polarity (negative), High Subjectivity.
# Neutral Fact: "The sky is blue and the grass is green."
# Result: Polarity near 0, Low Subjectivity.
# Sarcasm: "Oh great, another rainy day. Just what I wanted."
# Result: (Note: TextBlob often struggles with sarcasm and might give it a positive score because of the word "great".)

# from textblob import TextBlob
# if user_input:
#     blob = TextBlob(user_input)
#     sentiment = blob.sentiment
#     st.write("Sentiment Analysis from TextBlob:", sentiment)
    # st.write("Polarity: ", sentiment.polarity)
    # st.write("Subjectivity: ", sentiment.subjectivity)

# Use Transformer Model (Advanced NLP)
# from transformers import pipeline
# # Load the sentiment analysis pipeline
# sentiment_pipeline = pipeline("sentiment-analysis")
# if user_input:
#     sentiment_result = sentiment_pipeline(user_input)
#     st.write("Sentiment Analysis from Transformers:", sentiment_result)

# Improve UI (Make it Clean)
# st.sidebar.title("Options")
# task = st.sidebar.selectbox("Choose Task", ["Tokenize", "Sentiment"])

# if task == "Tokenize":
#     st.write(tokens)

# elif task == "Sentiment":
#     st.write(result)

# uploaded_file = st.file_uploader("Upload a text file")

# if uploaded_file:
#     text = uploaded_file.read().decode("utf-8")
#     st.write(text)

import streamlit as st
from nltk.tokenize import word_tokenize
# nltk.download('punkt_tab')
from nltk.corpus import stopwords
# nltk.download('stopwords')
from textblob import TextBlob

st.title("NLP Text Analyzer")

text = st.text_area("Enter text")

if text:
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in tokens if w.lower() not in stop_words]
    sentiment = TextBlob(text).sentiment

    st.write("Tokens:", tokens)
    st.write("Filtered:", filtered)
    st.write("Sentiment:", sentiment)
