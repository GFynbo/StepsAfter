from flask import Flask, render_template, request, url_for
from datetime import datetime
# from twilio.twiml.messaging_response import MessagingResponse
# from twilio.rest import Client

application = Flask(__name__)
# Find these values at https://twilio.com/user/account
# account_sid = "ACe5b4d18c96e93c3bc1053febe0331474"
# auth_token = "fcaea4bd6d12c9eab24d5c1e5a818b12"
# client = Client(account_sid, auth_token)


@application.route('/')
def home():
    return render_template('home.html')

@application.route('/after-an-od')
def after_an_od():
    return render_template('after-an-od.html')

@application.route('/facilities')
def facilities():
    return render_template('facilities.html')

@application.route('/help')
def hello():
    return 'Text (424) 297-5085 for immediate instructions on dealing with an overdose.'

# @application.route("/sms", methods = ['GET', 'POST'])
# def index():
#     from_number = request.values.get('Body', None)
#     if from_number in "erEREreR":
#         resp = MessagingResponse() #creates object
#         resp.message("STEP 1: CALL FOR HELP (DIAL 911).  \n STEP 2: CHECK FOR SIGNS OF OPIOID OVERDOSE. \n STEP 3: SUPPORT THE PERSON'S BREATHING. \n STEP 4: ADMINISTER NALOXONE. \n STEP 5: MONITOR THE PERSON'S RESPONSE.") #creates what to say
#         return str(resp)
#     if from_number in "seek help":
#         resp = MessagingResponse()
#         resp.message("Vist our website at stepsafter.com for more information regarding different substance abuse facilities.")
#         return str(resp)
#     if from_number in "secret message":
#         resp = MessagingResponse()
#         resp.message("THIS WAS CREATED IN THE BU HACKATHON OF 2017 FOR SAMHSA \n HOPE YOU ENJOY IT <3 \n IVE BEEN UP FOR 24 HOURS STRAIGHT")
#         return str(resp)

if __name__ == "__main__":
    application.run()
