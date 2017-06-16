from sensors_communication.sensors import TemperatureSensor
from sensors_communication.measure import Measure
import math

temperature_sensor = TemperatureSensor()
ph_sensor = PhSensor()
measure = Measure()

while True:
    measure.temperature = temperature_sensor.collect_data()
    measure.density = ph_sensor.collect_data()
    measure.push_callback()
