import math
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

class TemperatureSensor():
    def steinhart_hart(self, temp):
        return (float(temp)*5.0/(65535))/0.01

    def collect_data(self):
        temperature_samples = 100
        lm35_adc_sum = 0.0
        for i in range(0, temperature_samples):
            lm35_adc = adc.read_adc(0, gain=GAIN)
            lm35_adc_sum += lm35_adc
        lm35_adc_avg = lm35_adc_sum/temperature_samples
        return self.steinhart_hart(lm35_adc_avg)
