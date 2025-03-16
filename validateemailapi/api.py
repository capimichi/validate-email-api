from fastapi import FastAPI, Query
from pydantic import BaseModel
from validate_email import validate_email
import os
from dotenv import load_dotenv
from .models import EmailValidationRequest, EmailValidationResponse
import uvicorn

load_dotenv()

app = FastAPI(
    title="Validate Email API",
    description="API to validate email addresses",
    version="1.0.0",
    servers=[
        {
            "url": os.getenv("API_URL", "http://0.0.0.0:8000"),
            "description": "Server"
        },
    ]
)

@app.post("/validate-email/")
def post_validate_email(request: EmailValidationRequest):
    is_valid = validate_email(
        email_address=request.get_email_address(),
        check_format=request.get_check_format(),
        check_blacklist=request.get_check_blacklist(),
        check_dns=request.get_check_dns(),
        dns_timeout=request.get_dns_timeout(),
        check_smtp=request.get_check_smtp(),
        smtp_timeout=request.get_smtp_timeout(),
        smtp_helo_host=request.get_smtp_helo_host(),
        smtp_from_address=request.get_smtp_from_address(),
        smtp_skip_tls=request.get_smtp_skip_tls(),
        smtp_tls_context=request.get_smtp_tls_context(),
        smtp_debug=request.get_smtp_debug,
    )
    return EmailValidationResponse(is_valid=is_valid)

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=os.getenv("API_HOST", "0.0.0.0"), 
        port=int(os.getenv("API_PORT", 8000))
    )
