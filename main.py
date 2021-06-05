
import pyrebase
import requests
import json
from pusher_push_notifications import PushNotifications

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
device = 'chfwNH63TEqmYeAHRivkna:APA91bGK286s_Zik8R2-QhlLOZiUJm5YNxXxSA4nvpmPLniqjvqXGCVSRuAH7tH81NazZtoAtu60Cp2u9HSsKB82TngCQSbURwS7-Q2XLokGQies5eTQ2kNCwu-DNSbmTGPG9T8B95rG'
db = firebase.database()
beams_client = PushNotifications(
    instance_id='f800f676-a0af-4fee-be95-06a8d254a474',
    secret_key='4FB41C68E36B684C59D679ABA4A0803363C2AE1D794BACA6F8CDD9EBB8FEB845',
)


def stream_handler(message):
    print(message)
    if message['data'] > 500:
        print('5 is high')
        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = device

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: GAS',
                             'body': 'GAS Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                "/TopicName",
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("5").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 50:
        print('7 is high')
        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = device

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO',
                             'body': 'CO Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                '/TopicName',
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("7").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 500:
        print('135 is high')
        serverToken = 'AAAAwZW1mqA:APA91bEoA3eTrSYqk_TzGfDqL3zs8NijKvRuVCXt0cFyPlc1q1Y2X2iCxktKVtVtk8BRGq7NZ03WKc-esU1jmI68fsp4JuMPRohPDm4bjq4WunQeBgdFI3M3ItLsZv7r_oSl0_KnL7cC'
        deviceToken = device

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO2',
                             'body': 'CO2 Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                '/TopicName',
            'priority': 'high',
        }
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("135").stream(stream_handler, None)

