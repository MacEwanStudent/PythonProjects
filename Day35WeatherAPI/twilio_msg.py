from twilio.rest import Client
import os


class SendMsg:
  def __init__(self, message="hello world"):
    self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    self.client = Client(self.account_sid, self.auth_token)
    self.body= message

  def send_whatsapp(self):
    message = self.client.messages.create(
      from_='whatsapp:+14155238886',
      body=self.body,
      to='whatsapp:+15873402209'
    )
    print(message.sid)

  def set_message(self, msg):
    self.body=msg