import requests
import json
from sensors_communication.env_config import env
from sensors_communication.sensors import UltrasonicSensor

ultrasonic_sensor = UltrasonicSensor()

def check_ultrasonic_distance():
    ultrasonic_distance = ultrasonic_sensor.collect_data()
    print "ultrasonico DISTANCIA:"
    print ultrasonic_distance
    maximum_distance = 8
    sent = False
    if ultrasonic_distance > maximum_distance:
        if sent == False:
            send_push_notification()
            sent = True
	    print "There's no more sugar"
    else:
	sent = False
        print "There's still sugar"

def send_push_notification():
    url = env["server_address"]+"/api/reaction/addSugar"
    print url
    r = requests.get(url)
    print(r.json())

while True:
    check_ultrasonic_distance()
