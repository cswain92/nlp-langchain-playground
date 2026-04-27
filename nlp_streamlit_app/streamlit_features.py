import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Features Showcase")

# 1. Display a simple text
st.write("Welcome to the Streamlit Features Showcase! Here we will demonstrate various features of Streamlit.")

# 2. Display a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
st.write("Here is a simple DataFrame:")
st.dataframe(df)

# 3. Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.write("Here is a line chart of random data:")
st.line_chart(chart_data)