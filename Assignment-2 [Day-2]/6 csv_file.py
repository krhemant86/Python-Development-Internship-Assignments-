import requests
import pandas as pd
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


new_json = [
    {"time":str(timestamp),
     "lat":str(latitude),
     "long":str(longitude)
     }
]

df = pd.DataFrame(new_json)
print(df)
# df.to_csv("record.csv")