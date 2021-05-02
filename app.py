from flask import Flask, render_template
import requests
from searchAPI import returnSearch,returnMovieDetailsResponse,returnTVShowDetailsResponse

app = Flask(__name__,static_folder='./templates',static_url_path='/')
BASE_ROUTE = '/api/v1'

@app.route('/')
def index():
    return app.send_static_file('index.html')


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