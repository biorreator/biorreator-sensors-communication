from sensors_communication.sensors import TemperatureSensor
from sensors_communication.sensors import PhSensor
from sensors_communication.sensors import PressureSensor
from sensors_communication.sensors import UltrasonicSensor
from sensors_communication.measure import Measure
import math

import RPi.GPIO as GPIO
import time

temperature_sensor = TemperatureSensor()
ph_sensor = PhSensor()
pressure_sensor = PressureSensor()
ultrasonic_sensor = UltrasonicSensor()
measure = Measure()

# measure.temperature = temperature_sensor.collect_data()
# measure.pressureA = ph_sensor.collect_data() #change pressureA to ph
# measure.density = pressure_sensor.collect_data()
# measure.push_callback()
# print ultrasonic_sensor.collect_data()
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:

    GPIO.output(TRIG, False)
    print "Waitng For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
