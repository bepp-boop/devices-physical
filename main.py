import serial
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

url = "https://soft-d20bd-default-rtdb.firebaseio.com/";

# Fetch the service account key JSON file contents
cred = credentials.Certificate('soft-d20bd-firebase-adminsdk-ho640-7fec88a947.json')

# Initialize the app with a service account, granting admin privileges
default_app = firebase_admin.initialize_app(cred, {'databaseURL': url})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference("Data")

windows = ref.child("window")
windows.set(True)
door = ref.child("door")
door.set(True)
light = ref.child("light")
light.set(True)
smokeAlarm = ref.child("smokeAlarm")
smokeAlarm.set(True)
#When smoke alarm reach critical, send to firebase as true else false
soilDry = ref.child("soilDry")
soilDry.set(True)
#When soil moisture reach critical, send to firebase as true else false

arduino = serial.Serial('COM5', 9600, timeout=.1)

#Make a console that take input from user
def console():
    while True:
        command = input("Enter command: ")




while True:
    data = arduino.readline().decode().strip()
    if data:
        print(data)

