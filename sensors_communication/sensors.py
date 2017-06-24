import math
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time


adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

class TemperatureSensor():

    def collect_data(self):
        temperature_samples = 5
        ds18b20_sum = 0.0
        for i in range(0, temperature_samples):
            tfile = open("/sys/bus/w1/devices/28-041661cf4eff/w1_slave")
            text = tfile.read()
            tfile.close()
            secondline = text.split("\n")[1]
            ds18b20_data = secondline.split(" ")[9]
            ds18b20_temperature = float(ds18b20_data[2:])
            ds18b20_temperature = ds18b20_temperature/1000
            ds18b20_sum += ds18b20_temperature
        ds18b20_average = ds18b20_sum/temperature_samples
        return ds18b20_average

class PhSensor():

    def collect_data(self):
        ph_samples = 100
        ph_adc_sum = 0.0
        for i in range(0, ph_samples):
            ph_adc = adc.read_adc(1, gain=GAIN)
            tense = (ph_adc * 0.1875)/1000
            ph_adc = -5.7916 * tense + 22.933
            ph_adc_sum += ph_adc
        ph_adc_average = ph_adc_sum/ph_samples
        return ph_adc_average

class PressureSensor():

    def collect_data(self):
        pressure_samples = 100
        mp5500dp_adc_sum = 0.0
        for i in range(0, pressure_samples):
            mp5500dp1_adc = adc.read_adc(0, gain=GAIN)
            mp5500dp2_adc = adc.read_adc(2, gain=GAIN)
            tense_1 = (mp5500dp1_adc * 0.1875)/1000
            tense_2 = (mp5500dp2_adc * 0.1875)/1000
            zero_1 = 0.20
            zedo_2 = 0.19
            calibration_1 = tense_1 - zero_1
            calibration_2 = tense_2 - zero_2
            difference = (calibration_1 - calibration_2)/0.009
	    density = difference/(9.81*0.25) * 1000
            mp5500dp_adc_sum += density
        mp5500dp_adc_average = mp5500dp_adc_sum/pressure_samples
        return mp5500dp_adc_average

class UltrasonicSensor:

    def collect_data(self):
        GPIO.setmode(GPIO.BCM)
        TRIG = 23
        ECHO = 24

        print "Distance measurement in progress"

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

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
