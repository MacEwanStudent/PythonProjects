from twilio.rest import Client
import os
from mylib.myinfo import MyInfo


class SendMsg:
  def __init__(self, message="hello world"):
    # self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    # self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    self.body = message


    self.my_info = MyInfo()
    self.account_sid=self.my_info.get_info("TwilioInfo","ACCOUNT_SID")
    self.auth_token=self.my_info.get_info("TwilioInfo", "AUTH_TOKEN")
    self.client = Client(self.account_sid, self.auth_token)
    self.from_num = self.my_info.get_info("TwilioInfo","MY_TWILIO_PHONE")
    self.to_num = self.my_info.get_info("General", "MY_PHONE")

  def send_whatsapp(self):
    message = self.client.messages.create(
      from_=self.from_num,
      body=self.body,
      to=self.to_num
    )

  def set_message(self, msg):
    self.body=msg