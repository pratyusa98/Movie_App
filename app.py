from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/trend")
def trend():

	url = 'https://api.themoviedb.org/3/trending/movie/day?api_key=24229d94e4e0c003538fca41ba9cc128'
	search_trend_movie_response = requests.get(url).json()
	trend_movie=search_trend_movie_response["results"]

	return render_template('trending.html', trend_movie =trend_movie)




@app.route("/result",methods=['POST'])
def result():
	# search_movie = request.args.get('search_movie')
	search_movie = request.form['search']

	search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key=24229d94e4e0c003538fca41ba9cc128&query={}'.format(search_movie)
	search_movie_response = requests.get(search_movie_url).json()
	r=search_movie_response["results"]
	tr=search_movie_response["total_results"]
	id = r[:9]
	# title = search_movie_response.get['total_results']

	return render_template('result.html', data =r,total=tr)

@app.route("/movie/<int:id>")
def movie(id):

	id_movie = id

	id_url = "https://api.themoviedb.org/3/movie/{}?api_key=24229d94e4e0c003538fca41ba9cc128".format(id_movie)
	search_movie_response = requests.get(id_url).json()
	genres=search_movie_response["genres"]

	return render_template("single.html",movie = search_movie_response,genres=genres)


if __name__ == "__main__":
    app.run(debug=True)