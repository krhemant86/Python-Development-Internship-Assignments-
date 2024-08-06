import requests
import json

url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"Nasa"
}

data = requests.get(url,headers=header)
json_data = json.loads(data.text)
latitude = json_data["iss_position"]["latitude"]
longitude = json_data["iss_position"]["longitude"]
timestamp =json_data["timestamp"]

print('latitude:- ',latitude)
print('longitude:- ',longitude)
print('timestamp:- ',timestamp)
