import requests
import json
from sensors_communication.env_config import env

class Measure():
    def __init__(self):
        self.temperature = 0
        self.density = 0
        self.pressureA = 0
        self.pressureB = 0

    def push_callback(self):
        url = env["server_address"]+"/api/reaction/2bd80803-0bb1-4387-a6ed-0e4c9a144341/measures"
        data = {
            "temperature": self.temperature,
            "density": self.density,
            "pressureA": self.pressureA,
            "pressureB": self.pressureB,
        }
        data = json.dumps(data)
        print data
        print url
        # verify if there is some token auth for api
        r = requests.post(url, data=data)
        print(r.json())
