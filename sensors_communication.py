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

measure.temperature = temperature_sensor.collect_data()
measure.ph = ph_sensor.collect_data()
measure.density = pressure_sensor.collect_data()
measure.push_callback()
