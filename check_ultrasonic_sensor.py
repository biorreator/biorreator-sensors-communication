from sensors_communication.sensors import UltrasonicSensor

ultrasonic_sensor = UltrasonicSensor()

def check_ultrasonic_distance():
    ultrasonic_distance = ultrasonic_sensor.collect_data()
    print "ultrasonico DISTANCIA:"
    print ultrasonic_distance
    maximum_distance = 8
    sent = False
    if ultrasonic_distance > maximum_distance:
        if !sent:
            send_push_notification()
            sent = True
    else:
        console.log("There's still sugar")

def send_push_notification():
    url = env["server_address"]+"/api/addSugar"
    print url
    data = {}
    data = json.dumps(data)
    print data
    r = requests.post(url, headers={'Content-Type': 'application/json'}, data=data)
    print(r.json())

while True:
    check_ultrasonic_distance()
