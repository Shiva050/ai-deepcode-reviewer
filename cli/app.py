import streamlit as st
from main import query_llm

st.title("AI DeepCode Reviewer")
uploaded = st.file_uploader("Upload code file")

if uploaded:
    code = uploaded.read().decode()
    st.code(code)
    if st.button("Review Code"):
        review = query_ollama(f"Review this code:\n{code}")
        st.text_area("AI Review", review)