import streamlit as st
from app.reviewer import review_code
from app.utils import read_code_file

st.set_page_config(page_title="AI Deep Code Reviewer", layout="wide")
st.title("🧠 AI Deep Code Reviewer")
st.markdown("Upload your Python code and get instant AI-powered review and suggestions.")

uploaded_file = st.file_uploader("📄 Upload a `.py` file", type=["py"])

if uploaded_file:
    if not uploaded_file.name.endswith(".py"):
        st.warning("⚠️ Please upload a `.py` file.")
    else:
        code = read_code_file(uploaded_file)

        if "[Error]" in code:
            st.error(code.replace("[Error]", "❌"))
        else:
            st.code(code, language="python")

            if st.button("🚀 Review Code"):
                with st.spinner("Analyzing with AI..."):
                    try:
                        review = review_code(code)
                        if not review.strip():
                            st.error("❌ The review is empty. Please try again or check the code.")
                        else:
                            st.subheader("📋 AI Suggestions")
                            st.text_area("Review", review, height=400)
                    except Exception as e:
                        st.error(f"❌ Review failed: {e}")
else:
    st.info("⬆️ Upload a file to begin.")