import math
import Adafruit_ADS1x15

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
            ph_adc = (ph_adc * 0.1875)/1000
            ph_adc_sum += ph_adc
        ph_adc_average = ph_adc_sum/ph_samples
        return ph_adc_average

class PressureSensor():

    def collect_data(self):
        pressure_samples = 100
        mp5500dp_adc_sum = 0.0
        for i in range(0, pressure_samples):
            mp5500dp_adc = adc.read_adc(0, gain=GAIN)
            tense = (mp5500dp_adc * 0.1875)/1000
            mp5500dp_adc = (tense-0.189)/0.009
	    density = mp5500dp_adc/(9.81*0.22)
            mp5500dp_adc_sum += density 
        mp5500dp_adc_average = mp5500dp_adc_sum/pressure_samples
	print "MEDIA TENSAO:"
        return mp5500dp_adc_average
