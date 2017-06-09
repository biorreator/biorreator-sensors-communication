import requests
from sensors_communication.env_config import env

class Measure():
    def __init__(self):
        self.temperature = 0
        self.density = 0
        self.pressureA = 0
        self.pressureB = 0

    def push_callback(self):
        url = env["server_address"]+"/api/measures"
        data = {
            "measure": {
                "temperature": self.temperature,
                "density": self.density,
                "pressureA": self.pressureA,
                "pressureB": self.pressureB,
            }
        }
        # verify if there is some token auth for api
        r = requests.post(url, headers={'Authorization': 'Token '+'tokenx'}, data=data)
        print(r.json())
