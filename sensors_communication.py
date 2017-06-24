from sensors_communication.sensors import TemperatureSensor
from sensors_communication.sensors import PhSensor
from sensors_communication.sensors import PressureSensor
from sensors_communication.sensors import UltrasonicSensor
from sensors_communication.measure import Measure
import math
import os

temperature_sensor = TemperatureSensor()
ph_sensor = PhSensor()
pressure_sensor = PressureSensor()
ultrasonic_sensor = UltrasonicSensor()
measure = Measure()

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
    measure.temperature = temperature_sensor.collect_data()
    measure.ph = ph_sensor.collect_data()
    measure.density = pressure_sensor.collect_data()
    measure.push_callback()
    check_ultrasonic_distance()
    print "temp"
    print measure.temperature
    print "ph"
    print measure.ph
    print "density"
    print measure.density
