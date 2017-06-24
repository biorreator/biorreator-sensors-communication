import requests
import json
from sensors_communication.env_config import env

class Measure():
    def __init__(self):
        self.temperature = 0
        self.density = 0
        self.ph = 0

    def push_callback(self):
        url = env["server_address"]+"/api/reactions/881ba792-1ee8-422a-8d7c-a4fd44eff703/measures"
        print url
        data = {
            "temperature": self.temperature,
            "density": self.density,
            "ph": self.ph
        }
        data = json.dumps(data)
        print data
        r = requests.post(url, headers={'Content-Type': 'application/json'}, data=data)
        print(r.json())
