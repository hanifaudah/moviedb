from flask import Flask,request,render_template
from fetch import movie, movie_collection
from datetime import date
import json
import requests
app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def landing():
    if request.method == "GET":
        # top of the year
        year = date.today().year
        id_year = "http://api.themoviedb.org/3/discover/movie?api_key=95368f360e3dc457d2f213e11967e205&primary_release_year={}&sort_by=popularity.desc".format(year)
        top_year = movie_collection()
        top_year.results = []
        top_year.fetch(id_year)
        #top of genre
        genres = json.loads(requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=95368f360e3dc457d2f213e11967e205&language=en-US").text)["genres"]
        top_genre_collection = []
        for genre in genres:
            genre_id = "http://api.themoviedb.org/3/discover/movie?api_key=95368f360e3dc457d2f213e11967e205&with_genres={}&sort_by=popularity.desc".format(genre["id"])
            top_genre = movie_collection()
            top_genre.results = []
            top_genre.fetch(genre_id)
            top_genre_id = [top_genre.results,genre["name"]]
            top_genre_collection.append(top_genre_id)
        return render_template("home.html",top_year=top_year.results,year=year,top_genre=top_genre_collection)
    elif request.method == "POST":
        key_word = request.form["query"]
        id = "http://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=" + key_word
        movie_dict = movie_collection()
        movie_dict.results = []
        movie_dict.fetch(id)
        return render_template("landing.html",movie=movie_dict.results,key_word=key_word)

@app.route('/details/<id>',methods=["GET"])
def details(id):
    url = "http://api.themoviedb.org/3/movie/" + id + "?api_key=95368f360e3dc457d2f213e11967e205"
    data = json.loads(requests.get(url).text)
    data = movie(data["id"],data["title"],data["poster_path"],data["vote_average"],data["release_date"],data["overview"])
    return render_template("details.html",movie=data)

# if __name__=="__main__":
#     app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)