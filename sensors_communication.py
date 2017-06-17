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

while True:
    # measure.temperature = temperature_sensor.collect_data()
    # measure.pressureA = ph_sensor.collect_data() #change pressureA to ph
    # measure.density = pressure_sensor.collect_data()
    # measure.push_callback()
    ultrasonic_distance = ultrasonic_sensor.check_distance()
    print "DISTANCIA:"
    print ultrasonic_distance
    maximum_distance = 8
    if ultrasonic_distance > maximum_distance
        os.system("/home/pi/Desktop/pi2/bioreator-api/scripts/turn_on.py 22")
        print "PASSOU1"
    else
        os.system("/home/pi/Desktop/pi2/bioreator-api/scripts/turn_off.py 22")
        print "PASSOU2"
