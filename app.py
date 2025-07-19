import streamlit as st
from app.reviewer import review_code
from app.utils import read_code_file

st.set_page_config(page_title="AI Deep Code Reviewer", layout="wide")

st.title("AI Deep Code Reviewer")
st.markdown("Upload your Python code and get instant AI-powered review and suggestions.")

uploaded_file = st.file_uploader("📄 Upload a `.py` file", type=["py"])

if uploaded_file:
    code = read_code_file(uploaded_file)
    st.code(code, language="python")

    if st.button("Review Code"):
        with st.spinner("Analyzing code..."):
            review = review_code(code)
        st.subheader("📋 Review Feedback")
        st.text_area("AI Suggestions", review, height=400)