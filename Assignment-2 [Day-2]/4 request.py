

import requests
import json


url = "http://api.open-notify.org/iss-now.json"

data = requests.get(url)

data1 = json.loads(data.text)

lat = data1["iss_position"]["latitude"]
print('latitude:- ',latitude)