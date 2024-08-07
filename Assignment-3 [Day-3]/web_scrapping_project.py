import requests,json,pandas as pd
from datetime import datetime,timedelta


# define the time range
start_day = datetime(2024,5,1)
end_day = datetime(2024,6,30)

data_dates = []

cur_date = start_day
while cur_date <= end_day:
    date_str = cur_date.strftime("%Y-%m-%d")

    url = "https://vegetablemarketprice.com/api/dataapi/market/bihar/daywisedata?date=" + date_str

    header = {

                "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "Usr-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "sec-fetch-site": "same-origin",
        "cookie": "JSESSIONID=EFBD5BF0C820AA3BC815DB9769E0F25C; _ga=GA1.1.1260642287.1723005027; __gads=ID=6089d59fbf36470f:T=1723005024:RT=1723006868:S=ALNI_MZXZxt1v8qy9i959X44eiumAIY46A; __eoi=ID=e68a330d9f151d09:T=1723005024:RT=1723006868:S=AA-AfjaXO5sHi0wd_-rR1Otg_VTQ; _ga_2RYZG7Y4NC=GS1.1.1723005026.1.1.1723006880.0.0.0; FCNEC=%5B%5B%22AKsRol_ymKn9F6Ju4kje_wxllm36WapgP5SmO8FDNhjyv9FO4IKmydhGQwSQzxmwkO4s71PKPICJ3ycTn-OxbqRtUOpGxi0_ttfidE2s5qJOlrYjoUVwDiaNJXTh20DEcxPAqy2sZj4o2RFAkBG1XAgXHQEXUlNpLw%3D%3D%22%5D%5D",
        "Referer": "https://vegetablemarketprice.com/market/bihar/today",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    data= requests.get(url,headers=header)

    js_data = json.loads(data.text)

    
    for api in js_data["data"]:
        veg_id = str(api["id"])
        veg_name = str(api["vegetablename"])
        whole_price= str(api["price"])
        retail_price = str(api["retailprice"])
        shoping_mall_price = str(api["shopingmallprice"])
        unit_val = str(api["units"])
        veg_image = str(api["table"]["table_image_url"])

        new_js = {
            "Date" : date_str,
            "State_Name" : "Bihar",
            "veg_id":veg_id,
            "veg_name":veg_name,
            "whole_price":whole_price,
            "retail_price":retail_price,
            "shop_mall_price":shoping_mall_price,
            "unit_val":unit_val,
            "Vegetable_Image": veg_image
        }
        data_dates.append(new_js)
    
    cur_date += timedelta(days=1)

df  = pd.DataFrame(data_dates)
df.to_csv("vegetables_records.csv",index=False)