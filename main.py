from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe

all_movies = movies_data["original_title","poster_link","release_date","runtime","weighted_rating"]


# variables to store data

liked_movies = []
not_liked_movies = []
not_watched_movies = []

# method to fetch data from database

def assign_val():
  m_data = {
    "original_title": all_movies.iloc[0,0],
    "poster_link": all_movies.iloc[0,1],
    "release_date": all_movies.iloc[0,2],
    "duration": all_movies.iloc[0,3],
    "rating": all_movies.iloc[0,4]
  }

  return m_data

# /movies api

@app.route("/movies")
def get_movies():
  movies_data = assign_val()

  return jsonify({
    "data": movies_data,
    "status": "success"
  })

# /like api


@app.route("/like")

def get_liked_movie():
  global all_movies
  movies_data = assign_val()
  liked_movies.append(movies_data)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)

  return jsonify({
    "status": "success"
  })



# /dislike api

@app.route("/unlike")

def unliked_movies():
  global all_movies
  movies_data = assign_val()
  not_liked_movies.append(movies_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)


  return jsonify({
    "status": "success"
  })




# /did_not_watch api


@app.route("/not_watched_movies")

def get_not_watched_movies():
  global all_movies
  movies_data = assign_val()
  not_watched_movies.append(movies_data)
  all_movies.drop([0], inplace = True)
  all_movies = all_movies.reset_index(drop = True)


  return jsonify({
    "status": "success"
  })

if __name__ == "__main__":
  app.run()