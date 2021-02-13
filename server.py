from fastapi import FastAPI, Form, Header, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sendgrid.helpers.mail import Mail
import sendgrid
import os

tags_metadata = [
    {
        "name": "default",
        "description": "Do not try to hit this api from anywhere, it won't work 😉",
    }
]

app = FastAPI(title="E-Mail API", description="An API which uses SendGrid to send me mails about the forms submitted on my website!", version="1.0.0",
              docs_url=None, redoc_url="/docs", openapi_tags=tags_metadata)

apikey = os.environ['SENDGRID_KEY']
sg = sendgrid.SendGridAPIClient(apikey)

origins = [
    os.environ["ALLOWED_ORIGINS"]
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["default"])
async def welcome():
    return {
        "github": "https://github.com/sdabhi23/SendGrid-Mailer",
        "owner": "Shrey Dabhi <https://github.com/sdabhi23/>",
    }


@app.post("/contact", tags=["default"])
async def contact(response: Response, name: str = Form(None),
                  email: str = Form(None), subject: str = Form(None),
                  message: str = Form(None), origin: str = Header(None),
                  x_origin_token: str = Header(None)):
    if origin == os.environ["ALLOWED_ORIGINS"] and x_origin_token == os.environ["ORIGIN_TOKEN"]:
        message = Mail(
            from_email=os.environ["EMAIL"],
            to_emails=os.environ["EMAIL"],
            subject="Portfolio: Message from " + name,
            html_content=(
                """<b>Name:</b> {} <br/><br/> <b>Email Id:</b> {} <br/><br/> <b>Subject:</b> {} <br/><br/> <b>Message:</b> <br/><br/>{}""").format(name, email, subject, message)
        )
        response = sg.send(message)
        return {"status": response.status_code, "body": response.body, "headers": response.headers}
    else:
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"status": 403, "body": "You are not authorized to use this instance 😑"}
