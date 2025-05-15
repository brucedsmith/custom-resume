from fastapi import APIRouter, UploadFile, File, Form
from app.models import ResumeResponse
from app.core.processes import process_resume

router = APIRouter()

@router.post("/process", response_model=ResumeResponse)
async def process_resume_api(
    job_title: str = Form(...),
    job_description: str = Form(...),
    resume_file: UploadFile = File(...)
):
    modified_text = await process_resume(job_title, job_description, resume_file)
    return ResumeResponse(modified_resume_text=modified_text)
