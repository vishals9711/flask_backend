import requests
def filterNull(element):
    print(element)
    return element['poster_path'] != null

def returnSearch(name:str):
    url = 'https://api.themoviedb.org/3/search/multi'
    payload = {
        'api_key':"3b9a6ed72d9f555baf1e1ed7824b1314",
        'query':name
    }
    response = requests.get(url, params=payload).json()
    newResponse = remove_none(response['results'])
    response['results'] = newResponse
    return response

def returnMovieDetailsResponse(id:str):
    url = 'https://api.themoviedb.org/3/movie/' + id
    payload = {
        'api_key':"3b9a6ed72d9f555baf1e1ed7824b1314",
        'append_to_response':"recommendations,credits"
    }
    response = requests.get(url, params=payload).json()
    top6Cast = response['credits']['cast'][:6]
    response['credits']['cast'] = top6Cast
    response['credits']['crew']= []
    response['ott-details']  = (returnOTTDetails(response['imdb_id'])['streamingAvailability']['country'])
    response['providers'] = returnWatchProviders()
    return response

def returnTVShowDetailsResponse(id:int):
    url = 'https://api.themoviedb.org/3/tv/'+ id
    payload = {
        'api_key':"3b9a6ed72d9f555baf1e1ed7824b1314",
        'append_to_response':"watch/providers,recommendations,credits"

    }
    response = requests.get(url, params=payload).json()
    top6Cast = response['credits']['cast'][:6]
    response['credits']['cast'] = top6Cast
    response['credits']['crew']= []
    return response


def returnOTTDetails(imdb:str):
    url = 'https://ott-details.p.rapidapi.com/gettitleDetails'
    headers = {
    'x-rapidapi-key': "f5e16aaab0mshd5fc55058b588b7p19c432jsn2af2569eef34",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }
    querystring = {"imdbid":imdb}
    response = requests.get(url, headers=headers, params=querystring).json()
    return response


def remove_none(array):
    result = filter(lambda v: remove_non_obj(v), array)
    return list(result)

def remove_non_obj(obj):
    filtered = {k: v for k, v in obj.items() if v is not None}
    obj.clear()
    obj.update(filtered)
    return obj

def returnWatchProviders():
    url = 'https://api.themoviedb.org/3/watch/providers/movie'
    payload = {
        'api_key':"3b9a6ed72d9f555baf1e1ed7824b1314",
        'watch_region':"IN"
    }
    response = requests.get(url, params=payload).json()
    return response