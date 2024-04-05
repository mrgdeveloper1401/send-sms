import os
import requests
from kavenegar import *
from dotenv import load_dotenv

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
    def __init__(self, smsbody, smsNumber):
        self.username = 'tarabar.sina'
        self.password = 'Aa123456'
        self.smsbody = smsbody
        self.smmNumber = smsNumber
        self.GetId = 1
        self.nCmessage = 1
        self.nTypeSent = 2
        self.m_scheuleDate = None
        self.cDomainName = 'https://sms.smsnegar.com:443/fullrest/'
        self.cFormNumber = None
        self.nSpeedsms = 0
        self.nPeriodmin = 0
        self.cstarttime = None
        self.cEndTime = None

    @property
    def json_data(self):
        json_data = {
            'username': self.username,
            'password': self.password,
            'smsBody': self.smsbody,
            'smsNumber': self.smmNumber,
            'cFormNumber': self.cFormNumber,
            'GetId': self.GetId,
            'nCmessage': self.nCmessage,
            'nTypeSent': self.nTypeSent,
            'm_scheuleDate': self.m_scheuleDate,
            'cDomainName': self.cDomainName,
            'nSpeedsms': self.nSpeedsms,
            'nPeriodmin': self.nPeriodmin,
            'cstarttime': self.cstarttime,
            'cEndTime': self.cEndTime

        }
        return json_data

    def SendSms(self):
        url = self.cDomainName + 'SendSms'
        send_message = requests.post(url=url, json=self.json_data,
                                     )

# s1 = SmsNegar('درود وقت شما هم بخیر', '09171234567')
# s1.SendSms()
