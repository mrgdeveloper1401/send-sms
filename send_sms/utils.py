import os
import requests
from kavenegar import *
from dotenv import load_dotenv
from random import randint

load_dotenv()


# def send_sms(receptor, message, sender=None):
#     try:
#         api_key = os.environ.get('API_KEY')
#         api = KavenegarAPI(api_key)
#         params = {
#             'sender': '',
#             'receptor': receptor,
#             'message': message,
#         }
#         response = api.sms_send(params)
#         print(response)
#     except APIException as e:
#         print(e)
#     except HTTPException as e:
#         print(e)


class SmsNegar:
    def __init__(self, Smsbody, Mobiles):
        self.Smsbody = Smsbody
        self.Mobiles = Mobiles
        self.Id = str(randint(1, 999999))
        self.SenderNumber = '300060006060'
        self.UserName = 'tarabar.sina'
        self.Password = 'Aa123456'
        self.DomainName = 'yazd'

    @property
    def json_data(self):
        json_data = {
            'Smsbody': self.Smsbody,
            'Mobiles': [self.Mobiles],
            'UserName': self.UserName,
            'Password': self.Password,
            'DomainName': self.DomainName,
            'Id': self.Id,
            'SenderNumber': self.SenderNumber,
        }
        return json_data

    def send_sms(self):
        try:
            url = 'https://mehrafraz.com/fullrest/api/Send'
            send_message = requests.post(url=url, json=self.json_data)
            return send_message.status_code
        except Exception as e:
            print(e)


def send_sms_user(user_list, message):
    for u in user_list:
        full_name = u['نام و نام خوانوادگی']
        mobile = str(u['شماره همراه'])
        text = f'کاربر {full_name} {message}'
        send_message = SmsNegar(Smsbody=text, Mobiles=mobile)
        send_message.send_sms()
        print(send_message)
