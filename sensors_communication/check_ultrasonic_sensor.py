from sensors_communication.sensors import UltrasonicSensor

ultrasonic_sensor = UltrasonicSensor()

def check_ultrasonic_distance():
    ultrasonic_distance = ultrasonic_sensor.collect_data()
    print "ultrasonico DISTANCIA:"
    print ultrasonic_distance
    maximum_distance = 8
    if ultrasonic_distance > maximum_distance:
        os.system("scripts/turn_on.py 22")
    else:
        os.system("scripts/turn_off.py 22")

while True:
    check_ultrasonic_distance()
