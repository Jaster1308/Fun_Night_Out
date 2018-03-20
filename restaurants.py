# restaurant api caller
# restaurants.py
import requests
import ui

# api key for zomato
zomato_api = "57ca188bd1cb406464affeaa2690bb55"
# base url for requests in the Twin Cities area
base_url = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"
# header for api request
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}

def print_restaraunt(start):
    url = base_url + "&start=" + str(start) + "&count=1"
    response = requests.get(url, headers=header).json()
    # hopping through the json response and printing the necessary information
    for item in response["restaurants"]:
        r = item["restaurant"]
        location = r["location"]
        ui.message("\nName: " + r["name"])
        ui.message("Tags: " + r["cuisines"])
        ui.message("$ for 2: " + str(r["average_cost_for_two"]) + "$")
        ui.message("Address: " + location["address"] + "\n")

def main():
    start = 0
    choice = "y"
    ui.message("\n*Restaraunts in the Twin Cities Area*\n")
    while choice != "n":
        print_restaraunt(start)
        choice = ui.prompt_for_more()
        start+=1
    ui.message("\nGoodbye!\n")

main()
