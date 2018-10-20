from picamera import PiCamera
from gpiozero import Button
from signal import pause
from time import sleep
from datetime import datetime
import requests

TOKEN = "[token]"
URL = "[url]"

canera = PiCamera()
camera.resolution = (800, 600)
button = Button(2)

def sendImage():
    print("button was pressed")
    camera.start_preview()

    sleep(2)
    camera.capture("./image.jpg")

    camera.stop_preview()
    print("image was saved")

    files = {"[upload file name]": open("./image.jpg", "rb")}
    res = requests.post(URL, files=files)
    print(res.text)

print("ready")

button.when_pressed = sendImage

pause()