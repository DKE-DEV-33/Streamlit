import streamlit as st

st.title("Demo Streamlit App")

name = st.text_input("What's your name?")

if st.button("Submit"):
    st.write(f"Hello, {name}! 👋")
