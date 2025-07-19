import streamlit as st
from app.reviewer import review_code
from app.utils import read_code_file

st.set_page_config(page_title="AI Deep Code Reviewer", layout="wide")

st.title("AI Deep Code Reviewer")
st.markdown("Upload your Python code and get instant AI-powered review and suggestions.")

uploaded_file = st.file_uploader("📄 Upload a `.py` file", type=["py"])

if uploaded_file:
    try:
        code = read_code_file(uploaded_file)
        if "[Error]" in code:
            st.error("Unable to decode the uploaded file. Try saving it with UTF-8 encoding.")
        else:
            st.code(code, language="python")
            if st.button("🚀 Review Code"):
                with st.spinner("Analyzing code..."):
                    review = review_code(code)
                st.subheader("📋 Review Feedback")
                st.text_area("AI Suggestions", review, height=400)
    except Exception as e:
        st.error(f"Something went wrong: {e}")