# movies api caller
# DBmovie.py

import requests, os, ui, log


# HTTP request
def movie_api_top_5_movies_request():
    url = "https://api.themoviedb.org/3/movie/now_playing"
    key = os.environ.get('MOVIE_KEY')
    country = 'US'
    payload = {'api_key' : key, 'region' : country}
    response = requests.get(url, payload)

    return response

def convert_to_json(response):
    return response.json()

# print the top 5 movies from the response, used as display menu for movies
def print_movie_list(response):
    count = 0
    ui.print_to_user("")
    for i in response['results']:
        if count >= 5:
            break
        count+=1
        ui.print_to_user(str(count) + ". " + i['title'])
    ui.print_to_user('b. back')
    ui.print_to_user("")

# returns user selection for movie
def pick_movie():
    return input('Enter your selection: ')

# returns response for movie correlating to which_movie_number
def synopsis(which_movie_number, response):
    result_for_number = response['results'][which_movie_number]

    ui.print_to_user('\nMovie:')
    ui.print_to_user(result_for_number["title"])
    ui.print_to_user('\nRelease date:')
    ui.print_to_user(result_for_number["release_date"])
    ui.print_to_user('\nSynopsis:')
    ui.print_to_user(result_for_number['overview'])

# handle_movie_choice function for movie main menu display
def handle_movie_choice(choice, results):

    if choice >= "1" and choice <= "5":
        synopsis(int(choice)-1, results)

    else:
        ui.print_to_user("Please enter a valid selection")

# "main" function of DBmovie.py, kicks off movie api catcher and logic
def movie_start():

    ui.print_to_user("\n*Top 5 movies in Twin Cities Area Theaters*")
    results = movie_api_top_5_movies_request()
    # log response status code
    log.write_to_log("Status code for request to Movie API: " + str(results))
    json_obj = convert_to_json(results)


    quit = "b"
    choice = None

    while choice != quit:
        print_movie_list(json_obj)
        choice = pick_movie()
        handle_movie_choice(choice, json_obj)

    ui.print_to_user("\n*Main Menu")
    log.write_to_log("Back to main menu.")
