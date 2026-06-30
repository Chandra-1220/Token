import streamlit as st
from transformers import AutoTokenizer

# Page title
st.set_page_config(page_title="GPT-2 Tokenizer", page_icon="🤖")

st.title("🤖 GPT-2 Tokenizer")
st.write("Enter text below to see the generated tokens and their token IDs.")

# Load tokenizer only once
@st.cache_resource
def load_tokenizer():
    return AutoTokenizer.from_pretrained("gpt2")

tokenizer = load_tokenizer()

# User input
text = st.text_area("Enter a sentence")

# Button
if st.button("Tokenize"):
    if text.strip():

        # Tokenize text
        tokens = tokenizer.tokenize(text)

        # Convert tokens to IDs
        token_ids = tokenizer.convert_tokens_to_ids(tokens)

        st.subheader("Original Text")
        st.write(text)

        st.subheader("Tokens")
        st.write(tokens)

        st.subheader("Token IDs")
        st.write(token_ids)

        # Display token-ID mapping
        st.subheader("Token → Token ID")

        for token, token_id in zip(tokens, token_ids):
            st.write(f"**{token}** → {token_id}")

    else:
        st.warning("Please enter some text.")
