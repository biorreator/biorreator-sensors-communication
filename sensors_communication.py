from sensors_communication.sensors import TemperatureSensor
import requests
import os
from sensors_communication.env_config import env
import time
import math

temperature_sensor = TemperatureSensor()
sensors = [temperature_sensor]

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

def collect_temperature_sensor():
    temperature_samples = 100
    lm35_adc_sum = 0.0
    for i in range(0, temperature_samples):
        lm35_adc = adc.read_adc(0, gain=GAIN)
        lm35_adc_sum += lm35_adc
    lm35_adc_avg = lm35_adc_sum/temperature_samples
    return lm35_adc_avg

while True:
    sensors[0].push(collect_temperature_sensor())
