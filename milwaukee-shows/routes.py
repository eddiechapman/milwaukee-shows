from flask import request, current_app as app
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/' methods=['GET', 'POST'])
def sms():
    response = MessagingResponse()
    resp.message('Test response message')

    return str(resp)

