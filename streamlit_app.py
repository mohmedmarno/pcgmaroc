import streamlit as st
import pandas as pd

st.set_page_config(page_title="My First App")

# Main content goes here
st.title("Hello, Streamlit World! 👋")
st.write("This is where your interactive elements and data visualizations will go.")

# Example: Displaying a simple DataFrame
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)
st.dataframe(df)
