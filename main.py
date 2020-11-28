

import pyrebase
import requests
import json


firebaseConfig = {
    'apiKey': "AIzaSyAsYne7Q_5YyqQ012_e13oFjUCvnh2ZrSc",
    'authDomain': "airify-b9e29.firebaseapp.com",
    'databaseURL': "https://airify-b9e29.firebaseio.com",
    'projectId': "airify-b9e29",
    'storageBucket': "airify-b9e29.appspot.com",
    'messagingSenderId': "831440394912",
    'appId': "1:831440394912:web:7092a3143b601e83a907c5",
    'measurementId': "G-FQGPPP675Z"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()



def stream_handler(message):
    print(message)
    if message['data'] > 500:
        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = 'fMJAruTgShe3lkqnsprSJy:APA91bEP97Y6TSW_wHBWyd2TPu9K2bQRd1tiir7s0vWPgaxNptMRMKqz9iFQ4baihVIlyxkzzvbTKxkUrW_Y75XrsdITYenVW1H5zNy6Q1OCz5mukuEse_pA-XEl9ZT8kSmcloHBthA-'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: GAS',
                             'body': 'GAS Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                deviceToken,
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("5").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 500:

        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = 'fMJAruTgShe3lkqnsprSJy:APA91bEP97Y6TSW_wHBWyd2TPu9K2bQRd1tiir7s0vWPgaxNptMRMKqz9iFQ4baihVIlyxkzzvbTKxkUrW_Y75XrsdITYenVW1H5zNy6Q1OCz5mukuEse_pA-XEl9ZT8kSmcloHBthA-'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO',
                             'body': 'CO Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                deviceToken,
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("7").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 500:
        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = 'fMJAruTgShe3lkqnsprSJy:APA91bEP97Y6TSW_wHBWyd2TPu9K2bQRd1tiir7s0vWPgaxNptMRMKqz9iFQ4baihVIlyxkzzvbTKxkUrW_Y75XrsdITYenVW1H5zNy6Q1OCz5mukuEse_pA-XEl9ZT8kSmcloHBthA-'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO2',
                             'body': 'CO2 Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                deviceToken,
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("135").stream(stream_handler, None)

