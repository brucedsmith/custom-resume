import streamlit as st
import requests

st.title("Resume Optimizer")

job_title = st.text_input("Job Title")
job_description = st.text_area("Job Description")
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if st.button("Optimize Resume"):
    if job_title and job_description and resume_file:
        files = {
            "job_title": (None, job_title),
            "job_description": (None, job_description),
            "resume_file": (resume_file.name, resume_file, "application/pdf"),
        }
        response = requests.post("http://localhost:8000/api/v1/resume/process", files=files)
        if response.status_code == 200:
            st.subheader("Modified Resume:")
            st.text_area("Output", response.json()["modified_resume_text"], height=300)
        else:
            st.error("Something went wrong while processing.")
