"""
MIT License

Copyright (c) 2018 Shrey Dabhi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from fastapi import FastAPI, Form, Header, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sendgrid.helpers.mail import Mail
import sendgrid
import os

app = FastAPI(title="E-Mail API", description="An e-mail sending API for static sites using SendGrid and Python on Heroku. It now requires setting a safety token inorder to avoid unauthorised usage and spam messages.",
              version="1.0.0", docs_url=None, redoc_url=None)

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
