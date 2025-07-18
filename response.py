import requests
import json
print("\n EXAMPLE\n")
#define base url
base_url = "https://api.upcitemdb.com/prod/trial/lookup"
#define parameters
parameters = {"upc": "025000044908"}
#make Api request, passing in base URL and parameers
response = requests.get(base_url, params=parameters)
#parse the text from the API response using JSON schema
info = json.loads(response.text)
#extract the first item 
item = info["items"][0]
title = item["title"]
brand = item["brand"]
print("title", title)
print("brand", brand)