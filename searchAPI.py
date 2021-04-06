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
        'append_to_response':"watch/providers,recommendations,credits"
    }
    response = requests.get(url, params=payload).json()
    top6Cast = response['credits']['cast'][:6]
    response['credits']['cast'] = top6Cast
    response['credits']['crew']= []
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

def remove_none(array):
    result = filter(lambda v: remove_non_obj(v), array)
    return list(result)

def remove_non_obj(obj):
    filtered = {k: v for k, v in obj.items() if v is not None}
    obj.clear()
    obj.update(filtered)
    return obj