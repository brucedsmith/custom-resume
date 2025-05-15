import fitz
import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_text_from_pdf(file_bytes: bytes) -> str:
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        return "".join([page.get_text() for page in doc])

def call_openai(job_title: str, job_description: str, resume_text: str) -> str:
    prompt = f"""
You are a resume optimization assistant.

Given the following:

Job Title:
{job_title}

Job Description:
{job_description}

Candidate's Resume:
{resume_text}

Please tailor the resume so that it matches the job description as closely as possible.
Improve wording, emphasize relevant skills, and update unrelated content to make it relevant.

Only return the full improved resume.
"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # You can upgrade to gpt-4 if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message['content']
