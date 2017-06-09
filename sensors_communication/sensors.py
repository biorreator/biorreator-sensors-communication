from abc import ABCMeta, abstractmethod
from collections import deque
import requests
from sensors_communication.env_config import env
import math

class Sensor():
    __metaclass__ = ABCMeta
    def __init__(self):
        self.last_sended = -1

    @classmethod
    @abstractmethod
    def limiar(cls):
        pass

    @abstractmethod
    def push_callback(self, item):
        pass

    def diff(self, val1, val2):
        maxv = max(val1, val2)
        minv = min(val1, val2)
        return 100. - 100.*minv/maxv

    def push(self, item):
        self.push_callback(item)

class TemperatureSensor(Sensor):
    @classmethod
    def limiar(cls):
        return 2

    def steinhart_hart(self, temp):
        return (float(temp)*5.0/(65535))/0.01

    def push_callback(self, item):
        item = self.steinhart_hart(item)
        url = env["server_address"]+"/api/temperatures"
        if (self.diff(item, self.last_sended) > TemperatureSensor.limiar()):
            item = int(item)
            self.last_sended = item
            data = {
                'temperature': item
            }
            r = requests.post(url, headers={'Authorization': 'Token '+self.token}, data=data)
            print(r.json())
        else:
            print("skip...")
