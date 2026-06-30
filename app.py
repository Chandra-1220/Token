import streamlit as st

st.title("GPT-2 Tokenizer")

text = st.text_input("Enter text")

if st.button("Submit"):
    st.write("You entered:", text)
