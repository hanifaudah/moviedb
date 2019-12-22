from flask import Flask,request,render_template
from fetch import movie, movie_collection
import json
import requests
app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def landing():
    if request.method == "GET":
        return render_template("landing.html")
    elif request.method == "POST":
        key_word = request.form["query"]
        id = "http://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=" + key_word
        movie_dict = movie_collection()
        movie_dict.results = []
        movie_dict.fetch(id)
        return render_template("landing.html",movie=movie_dict.results)

@app.route('/details/<id>',methods=["GET"])
def details(id):
    url = "http://api.themoviedb.org/3/movie/" + id + "?api_key=95368f360e3dc457d2f213e11967e205"
    data = json.loads(requests.get(url).text)
    data = movie(data["id"],data["title"],data["poster_path"],data["vote_average"],data["release_date"],data["overview"])
    return render_template("details.html",movie=data)

# if __name__=="__main__":
#     url = "http://api.themoviedb.org/3/movie/557?api_key=95368f360e3dc457d2f213e11967e205"
#     data = json.loads(requests.get(url).text)
#     print(data["id"])