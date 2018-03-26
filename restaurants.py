# restaurant api caller
# restaurants.py
import requests
import ui
import os

# api key for zomato
# zomato_api = os.environ.get("ZOMATO_API_KEY") # Response 403 for bad api key
zomato_api = "57ca188bd1cb406464affeaa2690bb55"
# base url for requests in the Twin Cities area
base_url = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"
# header for api request
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}

# function print_restaurant, takes start which is int value of which restaurant is printed
def print_restaraunt(start):
    # adds on to base_url to create new query with start position passed in and count of 1
    url = base_url + "&start=" + str(start) + "&count=1"
    # raw_data from API request
    raw_data = requests.get(url, headers=header)
    # ui.message(raw_data) # response 200 for raw_data returned
    # json_obj of raw_data
    json_obj = raw_data.json()
    # hopping through the json_obj and printing the necessary information
    for item in json_obj["restaurants"]:
        restaurant = item["restaurant"]
        location = restaurant["location"]
        ui.message("\nName: " + restaurant["name"])
        ui.message("Tags: " + restaurant["cuisines"])
        ui.message("$ for 2: " + str(restaurant["average_cost_for_two"]) + "$")
        ui.message("Address: " + location["address"] + "\n")

# main function
def main():
    # init start to 0
    start = 0
    # init choice to "y"
    choice = "y"
    ui.message("\n*Restaraunts in the Twin Cities Area*")
    # while loop prompting user if they want info on other restaurants
    while choice != "n":
        if choice == "y":
            print_restaraunt(start)
            choice = ui.prompt_for_more()
            start+=1
        else:
            ui.message("Please enter y or n:\n")
            choice = ui.prompt_for_more()
            continue
    ui.message("\nGoodbye!\n")

# call main function
main()

# questions
# 1. Is it smart to do logging through a whole different file?
# 2. Testing the api calls, do we just test for responses as in if bad api, 403?
