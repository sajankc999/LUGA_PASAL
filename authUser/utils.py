from twilio.rest import Client
from dotenv import load_dotenv
import os
import pyotp
from datetime import datetime,timedelta


load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
from_=os.getenv('from_')

client = Client(account_sid, auth_token)


def Send_otp_whatsapp(number,otp):
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    # from_=os.getenv('from_')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_=os.getenv('from_'),
    body= f'your verification code for Luga pasal is  ::\n{otp}',
    to=f'whatsapp:+977{number}'
    )

    print(message.sid)

def send_otp(request):
    totp = pyotp.TOTP(pyotp.random_base32(),interval=15*60)
    generated_otp = totp.now()
    request.session['otp_secret_key']=totp.secret
    valid_date = datetime.now()+timedelta(minutes=15)
    request.session['otp_valid_date']=str(valid_date)
    try:
        Send_otp_whatsapp(request.data.get('phone_number'),generated_otp)
    except Exception as e:
        raise Exception(e)