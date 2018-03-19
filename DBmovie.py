import requests
import functools
import os
import timeit


@functools.lru_cache(maxsize=128)
def shows():
    url = "https://api.themoviedb.org/3/movie/now_playing"

    keys = os.environ.get('key')

    country = 'US'

    payload = {'api_key' : keys, 'region' : country}
    response = requests.get(url, payload).json()
    print('')
    print('Top five recently released movies:')
    print('1:', response["results"][0]["title"])
    print('2:', response["results"][1]["title"])
    print('3:', response["results"][2]["title"])
    print('4:', response["results"][3]["title"])
    print('5:', response["results"][4]["title"],'\n')

    topFive = response["results"][0]["overview"]
    topFive1 = response["results"][1]["overview"]
    topFive2 = response["results"][2]["overview"]
    topFive3 = response["results"][3]["overview"]
    topFive4 = response["results"][4]["overview"]

    syns = 'url', keys, country, payload, response, topFive, topFive1, topFive2, topFive3, topFive4
    return syns

def pick():
    choice = input("Would you like an overview for one of the movies?\nType 'yes' or 'no': ")
    if choice.lower() == "yes":
        print("\nSelect movie by order number: ")
    else:
        print('\nGoodbye!')
        exit()

def syns(url, keys, country, payload, response, topFive, topFive1, topFive2, topFive3, topFive4):
    choices = input('choice: ')
    if choices == '1':
        print('\nMovie:')
        print(response["results"][0]["title"])
        print('\nRelease date:')
        print(response["results"][0]["release_date"])
        print('\nSynopsis:')
        print(topFive,'\n')
        check_again()
    elif choices == '2':
        print('\nMovie:')
        print(response["results"][1]["title"])
        print('\nRelease date:')
        print(response["results"][1]["release_date"])
        print('\nSynopsis:')
        print(topFive1,'\n')
        check_again()
    elif choices == '3':
        print('\nMovie:')
        print(response["results"][2]["title"])
        print('\nRelease date:')
        print(response["results"][2]["release_date"])
        print('\nSynopsis:')
        print(topFive2,'\n')
        check_again()
    elif choices == '4':
        print('\nMovie:')
        print(response["results"][3]["title"])
        print('\nRelease date:')
        print(response["results"][3]["release_date"])
        print('\nSynopsis:')
        print(topFive3,'\n')
        check_again()
    elif choices == '5':
        print('\nMovie:')
        print(response["results"][4]["title"])
        print('\nRelease date:')
        print(response["results"][4]["release_date"])
        print('\nSynopsis:')
        print(topFive4,'\n')
        check_again()

def check_again():
    search_again = input("Choose another movie or quit. \nType 'q' to quit: ")
    if search_again.lower() == 'yes':
        main()
    else:
        search_again == 'q'
        print('\nGoodbye!')
        exit()

def main():
    results = shows()
    option = pick()
    syns(*results)

main()
