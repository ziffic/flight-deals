from twilio.rest import Client
import connect

TWILIO_SID = connect.TWILIO_SID
TWILIO_AUTH_TOKEN = connect.TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = connect.TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER = connect.TWILIO_VERIFIED_NUMBER


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
