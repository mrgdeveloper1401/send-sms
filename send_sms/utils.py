import os

from kavenegar import *


def send_single_sms_signals(receptor, message, sender):
    try:
        api_key = os.environ.get('API_KEY')
        api = KavenegarAPI(api_key)
        params = {
            'sender': f'{sender}',
            'receptor': f'{receptor}',
            'message': f'{message}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
