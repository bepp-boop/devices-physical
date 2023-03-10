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
door = ref.child("door")
light = ref.child("light")
smokeAlarm = ref.child("smokeAlarm")
#When smoke alarm reach critical, send to firebase as true else false
soilDry = ref.child("soilDry")
#When soil moisture reach critical, send to firebase as true else false

arduino = serial.Serial('COM5', 9600, timeout=.1)

#Make a console that take input from user


while True:
    command = input("Enter command: ")
    data = arduino.readline().decode().strip()
    if command == "w":
        data = windows.get()
        if data == True:
            windows.set(False)
            arduino.write(b'w')
            print("Window is closed")
        else:
            windows.set(True)
            arduino.write(b'w')
            print("Window is opened")
    elif command == "d":
        data = door.get()
        if data == True:
            door.set(False)
            arduino.write(b'd')
            print("Door is closed")
        else:
            door.set(True)
            arduino.write(b'd')
            print("Door is opened")
    elif command == "l":
        data = light.get()
        if data == True:
            light.set(False)
            arduino.write(b'l')
            print("Light is off")
        else:
            light.set(True)
            arduino.write(b'l')
            print("Light is on")


