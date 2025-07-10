This project is a Movie Recommender System built using Python, Streamlit, and The Movie Database (TMDb) API. The app recommends movies similar to a movie selected by the user and displays key details such as posters, overviews, genres, ratings, and trailers.

🚀 Demo
You can run this project locally using Streamlit. When launched, it provides a clean and interactive UI where users can:

Select a movie

See the top 5 recommended movies

View posters, descriptions, genres, and ratings

Watch the trailers directly in the app

🔍 How It Works
The project consists of two main components:

1. movies-recommender-system.ipynb
This Jupyter notebook performs the data preparation and builds the recommendation logic:

Loads a movie dataset.

Uses cosine similarity to find similar movies based on pre-computed features (details from this file are inferred as it wasn't directly examined in code form).

Saves the processed movie list and similarity matrix into two pickle files:

movie_list.pkl

similarity.pkl

2. app.py
This is the main Streamlit app that:

Loads the saved movie_list.pkl and similarity.pkl.

Uses the TMDb API to fetch additional movie details like:

Poster image

Genres

Rating

Overview

YouTube trailer link

Displays movie recommendations in an attractive, interactive format.

Handles API retries and network errors gracefully.

🛠️ Technologies Used
Python

Streamlit: Web app framework

Pickle: For saving and loading the dataset and similarity matrix

TMDb API: For fetching movie details

Requests: For API calls with a retry mechanism

Pandas: Data manipulation in the notebook

Cosine Similarity: For the recommendation logic

✅ Features
Movie title search and selection.

Shows top 5 recommended movies.

Displays:

Movie poster

Title and genres

IMDb-like rating

Brief overview

Embedded YouTube trailer

Responsive UI using Streamlit.

Graceful error handling when API requests fail.



