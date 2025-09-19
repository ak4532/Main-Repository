import streamlit as st

# Title
st.title("Hello, Streamlit!")

# Write some text
st.write("Welcome to my  first Streamlit app.")

# Addd a slider

number = st.slider("Pick a number", 1 , 10)

# Display the Result

st.write(f"You picked: {number}")

