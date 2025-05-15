from fastapi import UploadFile
from app.utils.helpers import extract_text_from_pdf, call_openai



async def process_resume(job_title: str, job_description: str, resume_file: UploadFile) -> str:
    contents = await resume_file.read()
    original_text = extract_text_from_pdf(contents)

    tailored_resume = call_openai(job_title, job_description, original_text)

    return tailored_resume

