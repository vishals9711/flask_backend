from flask import Flask
import requests
from searchAPI import returnSearch,returnMovieDetailsResponse,returnTVShowDetailsResponse

app = Flask(__name__)
BASE_ROUTE = '/api/v1'
@app.route(BASE_ROUTE + '/<string:name>')
def search(name):
    return returnSearch(name)

@app.route(BASE_ROUTE + '/movie/<string:id>')
def movieSearch(id):
    return returnMovieDetailsResponse(id)

@app.route(BASE_ROUTE + '/tv_show/<string:id>')
def tvShowSearch(id):
    return returnTVShowDetailsResponse(id)

if __name__ == '__main__':
    app.run(debug=True)