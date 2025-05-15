from pydantic import BaseModel

# class ResumeRequest(BaseModel):
#     job_title: str
#     job_description: str

class ResumeResponse(BaseModel):
    modified_resume_text: str