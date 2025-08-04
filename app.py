import streamlit as st
import requests

st.set_page_config(page_title="Career Counseling AI", layout="centered")
st.title("🎓 Agentic Career Counseling Companion")

st.markdown("Get a personalized career path using your skills and interests.")

skills = st.text_area("🔧 Your Skills (comma-separated)", placeholder="e.g., Python, SQL")
interests = st.text_input("💡 Your Interests", placeholder="e.g., Cloud, AI")

if st.button("Get Career Path"):
    if not skills or not interests:
        st.warning("Please enter both skills and interests.")
    else:
        with st.spinner("Thinking..."):
            res = requests.post("http://127.0.0.1:8000/career-recommend", json={
                "skills": skills,
                "interests": interests
            })
            response = res.json()
            st.success(response["career_path"])
