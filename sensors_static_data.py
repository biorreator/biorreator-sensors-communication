from sensors_communication.sensors import TemperatureSensor
from sensors_communication.sensors import PhSensor
from sensors_communication.sensors import PressureSensor
from sensors_communication.measure import Measure
import math
import os

temperature_sensor = TemperatureSensor()
ph_sensor = PhSensor()
pressure_sensor = PressureSensor()
measure = Measure()

def get_sensors_data:
    measure.temperature = temperature_sensor.collect_data()
    measure.ph = ph_sensor.collect_data()
    measure.density = pressure_sensor.collect_data()

def show_sensors_data:
    print measure.temperature
    print measure.ph
    print measure.density

get_sensors_data()
show_sensors_data()
