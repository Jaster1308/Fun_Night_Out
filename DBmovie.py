# movies api caller
# DBmovie.py

import requests
import os
import ui

# HTTP request
def movie_api_top_5_movies_request():
    url = "https://api.themoviedb.org/3/movie/now_playing"
    key = os.environ.get('MOVIE_KEY')
    country = 'US'
    payload = {'api_key' : key, 'region' : country}
    response = requests.get(url, payload).json()

    return response

# print the top 5 movies from the response, used as display menu for movies
def print_movie_list(response):
    count = 0
    ui.message("")
    for i in response['results']:
        if count >= 5:
            break
        count+=1
        ui.message(str(count) + ". " + i['title'])
    ui.message('b. back')
    ui.message("")

# returns user selection for movie
def pick_movie():
    return input('Enter your selection: ')

# returns response for movie correlating to which_movie_number
def synopsis(which_movie_number, response):
    result_for_number = response['results'][which_movie_number]

    ui.message('\nMovie:')
    ui.message(result_for_number["title"])
    ui.message('\nRelease date:')
    ui.message(result_for_number["release_date"])
    ui.message('\nSynopsis:')
    ui.message(result_for_number['overview'])

# handle_movie_choice function for movie main menu display
def handle_movie_choice(choice, results):

    if choice >= "1" and choice <= "5":
        synopsis(int(choice)-1, results)

    else:
        ui.message("Please enter a valid selection")

# "main" function of DBmovie.py, kicks off movie api catcher and logic
def movie_start():

    ui.message("\n*Top 5 movies in Twin Cities Area Theaters*")
    results = movie_api_top_5_movies_request()

    quit = "b"
    choice = None

    while choice != quit:
        print_movie_list(results)
        choice = pick_movie()
        handle_movie_choice(choice, results)

    ui.message("\n*Main Menu")
