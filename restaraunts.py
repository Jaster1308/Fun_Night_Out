import requests

# api key for zomato
zomato_api = "57ca188bd1cb406464affeaa2690bb55"
# base url for requests
base_url = "https://developers.zomato.com/api/v2.1/search?"
# city name variable
city = "Twin Cities"
# entity_id var that correlates to twin cities location
entity_id = "826"

restaraunts = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"

header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}

response = requests.get(restaraunts, headers=header).json()

print(response["results_found"])
print(response["results_start"])
print(response["results_shown"])

for item in response["restaurants"]:
    r = item["restaurant"]
    print(r["name"])
