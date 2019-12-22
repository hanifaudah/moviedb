# Importing libs
import requests
import json

# Main dictionary
movie_dict = {}

# Main movie class
class movie:
    def __init__(self,title="None",poster_url="None",score="None",date="None",overview="None"):
        self.title = title
        self.poster = "http://image.tmdb.org/t/p/w200" + str(poster_url)
        self.score = score
        self.date = date
        self.overview = overview

class movie_collection:
    def __init__(self,results=[]):
        self.results = results
    def fetch(self,url):
        results = json.loads(requests.get(url).text)["results"]
        for i in results:
            self.results.append(movie(i["title"],i["poster_path"],i["vote_average"],i["release_date"],i["overview"]))

if __name__=="__main__":
    mov = movie_collection()
    mov.fetch("http://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=spiderman")
    for i in mov.results:
        print(i.title,i.poster,i.score,i.date,i.overview)
        print()
        
