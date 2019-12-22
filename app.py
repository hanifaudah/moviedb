from flask import Flask,request,render_template
from fetch import movie, movie_collection
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