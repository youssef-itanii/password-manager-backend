import os
import json
from twilio.rest import Client
from config_file_handler import read_config_file
from query_handler import exec_query_with_records
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
class SMS_Client:
    def __init__(self , config_file = "config.ini" , config_file_path = os.path.dirname(__file__)):

        self.config_file = config_file
        self.config_file_path = config_file_path
        self.account_sid , self.auth_token = read_config_file(self.config_file_path , self.config_file , "twilio.credentials" , ["account_sid" , "auth_token"])
        self.client = Client(self.account_sid, self.auth_token)
   
    @staticmethod
    def generate_verification_message( profile_id):
        data = exec_query_with_records("EXEC Code_get "+str(profile_id))
        data = json.loads(data[0][0])[0]
        name = data["name"]
        verification_code = data["verification code"]
        phone_no = data["phone_no"]

        message = f"Hello! Here's your verification code: {verification_code} for PManager. If you did not sign up, please ignore this SMS "
        return phone_no , message



    def send_verification_message(self , id , phone_number = "" , message_body = ""):
        if phone_number == "" and message_body == "":
            phone_number , message_body = SMS_Client.generate_verification_message(id)
        print(phone_number)
        print(message_body)
        message = self.client.messages.create(
                                    body = message_body,
                                    from_= "+15128775184",
                                    to = "+"+phone_number
                                )
        print(message.sid)
