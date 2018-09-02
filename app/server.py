from app import app
from flask import render_template, request,jsonify
import sendgrid
import os

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/contact", methods=['POST'])
def contact():
    if request.method == 'POST':
        apikey = os.environ['SENDGRID_KEY']
        sg = sendgrid.SendGridAPIClient(apikey=apikey)
        data = {
            "personalizations": [
                {
                    "to": [
                        {
                          "email": "" # add your email address here
                        }
                    ],
                    "subject": "Portfolio: Message from " + str(request.form["name"])
                }
            ],
            "from": {
                "email": str(request.form["email"]),
                "name": str(request.form["name"])
            },
            "content": [
                {
                    "type": "text/plain",
                    "value": "Subject: " + str(request.form["subject"]) + "\n\nMessage:\n\n" + str(request.form["message"])
                }
            ]
        }
        response = sg.client.mail.send.post(request_body=data)
        return jsonify({"status": str(response.status_code)})