from sensors_communication.sensors import TemperatureSensor
from sensors_communication.sensors import PhSensor
from sensors_communication.sensors import PressureSensor
from sensors_communication.measure import Measure
import math

temperature_sensor = TemperatureSensor()
ph_sensor = PhSensor()
pressure_sensor = PressureSensor()
measure = Measure()

while True:
    measure.temperature = temperature_sensor.collect_data()
    measure.pressureA = ph_sensor.collect_data() #change pressureA to ph
    measure.density = pressure_sensor.collect_data()
    measure.push_callback()
