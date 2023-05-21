import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
flipkart_url = "https://flipkart.dvishal485.workers.dev/search/"
men_key = "men-cloth"
women_key = "women-cloth"
kid_key = "kids-cloth"
keywords = [men_key, women_key, kid_key]
name = []
link = []
for i in range(len(keywords)):
    response_API = requests.get(flipkart_url + keywords[i])
    parse_json = json.loads(response_API.text)
    total_results = parse_json["total_result"]
    # print(parse_json["result"][0])


    for j in range(total_results):
        name.append(parse_json["result"][j]["name"])
        link.append(parse_json["result"][j]["link"])

df = pd.DataFrame(columns=["name","link"])
df["name"] = name
df["link"] = link

df.to_csv("flipkart.csv")
