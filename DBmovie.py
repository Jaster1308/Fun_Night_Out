import requests
import os
#HTTP request
def movie_api_top_5_movies_request():
    url = "https://api.themoviedb.org/3/movie/now_playing"
    key = os.environ.get('MOVIE_KEY')
    country = 'US'
    payload = {'api_key' : key, 'region' : country}
    response = requests.get(url, payload).json()

    return response

def print_movie_list(response):
    for i in response['results']:
        print(i['title'])

def pick_movie():
    return int(input('Enter number 1 through 5: ')) ##TODO validtaion


def synopsis(which_movie_number, response):
    result_for_number = response['results'][which_movie_number]

    print('\nMovie:')
    print(result_for_number["title"])
    print('\nRelease date:')
    print(result_for_number["release_date"])
    print('\nSynopsis:')
    print(result_for_number['overview'])


def check_again():
     search_again = input("Choose another movie or quit. \nType 'q' to quit: ")
     if search_again.lower() == 'yes':
         main()
     else:
         search_again == 'q'
         print('\nGoodbye!')
         exit()

def main():
    results = movie_api_top_5_movies_request()
    print_movie_list(results)
    which_movie = pick_movie()
    synopsis(which_movie, results)

main()
