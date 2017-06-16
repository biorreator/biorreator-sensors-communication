import math
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

class TemperatureSensor():
    def collect_data(self):
        temperature_samples = 100
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
