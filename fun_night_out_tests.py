# fun_night_out_tests

import os, requests, nose, restaurants, log

# using third party nose library for mock api testing

# test for restaurant api call with a valid api key
def test_restaurant_api_good_key():

    log.write_to_log("Testing restaurant api call with valid API key")
    # base information needed for restaurant api call
    zomato_api = os.environ.get("FOOD_KEY")
    base_url = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}
    url = base_url + "&start=1&count=1"

    # make request for test
    response = requests.get(url, headers=header)

    # test the Response
    nose.tools.assert_true(response.ok)

# test for restaurant api call with a fake api key
def test_restaurant_api_bad_key():

    log.write_to_log("Testing restaurant api call with invalid API key")
    # base information needed for restaurant api call, with fake key
    zomato_api = "12345"
    base_url = "https://developers.zomato.com/api/v2.1/search?entity_id=826&entity_type=city"
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": zomato_api}
    url = base_url + "&start=1&count=1"

    # make request for test
    response = requests.get(url, headers=header)

    # test the Response
    nose.tools.assert_false(response.ok)

# test for movie api call with a valid api key
def test_movie_api_good_key():

    log.write_to_log("Testing movie api call with valid API key")
    # base information needed for movie api call
    url = "https://api.themoviedb.org/3/movie/now_playing"
    key = os.environ.get('MOVIE_KEY')
    country = 'US'
    payload = {'api_key' : key, 'region' : country}

    # make request for test
    response = requests.get(url, payload)

    # test the response
    nose.tools.assert_true(response.ok)

# test for movie api call with a fake api key
def test_movie_api_bad_key():

    log.write_to_log("Testing movie api call with invalid API key")
    # base information needed for movie api call, with fake key
    url = "https://api.themoviedb.org/3/movie/now_playing"
    key = "12345"
    country = 'US'
    payload = {'api_key' : key, 'region' : country}

    # make request for test
    response = requests.get(url, payload)

    # test the response
    nose.tools.assert_false(response.ok)

if __name__ == '__main__':
    nose.main()
