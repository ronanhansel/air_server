import pyrebase
import requests
import json
import os

firebaseConfig = {
    'apiKey': os.getenv('apiKey'),
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
serverToken = os.getenv('serverToken')

def stream_handler(message):
    print(message)
    if message['data'] > 500:
        print('5 is high')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: GAS',
                             'body': 'GAS Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                '/topics/TopicName',
            'priority': 'high',
        }
        requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("5").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 35:
        print('7 is high')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO',
                             'body': 'CO Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                '/topics/TopicName',
            'priority': 'high',
        }
        requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("7").stream(stream_handler, None)


def stream_handler(message):
    print(message)
    if message['data'] > 1000:
        print('135 is high')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
            'notification': {'title': 'NGUY HIỂM: CO2',
                             'body': 'CO2 Đang ở mức độ đáng cảnh báo: ' + str(message['data']) + ' ppm'
                             },
            'to':
                '/topics/TopicName',
            'priority': 'high',
        }
        requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))


my_stream = db.child("135").stream(stream_handler, None)

