# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit. The application recommends the top 5 movies similar to a movie selected by the user and fetches movie details such as posters, genres, ratings, overviews, and trailers using the TMDb API.

## ✨ Features

- Select a movie from the available movie list
- Get the top 5 similar movie recommendations
- Display movie posters
- Show movie ratings and genres
- Read movie overviews
- Watch movie trailers
- Fetch movie details using the TMDb API
- Interactive web interface using Streamlit
- Handles API and connection errors

## 🛠️ Tech Stack

- **Python**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Scikit-learn** – CountVectorizer and Cosine Similarity
- **Streamlit** – web application
- **Requests** – API requests and retry handling
- **Pickle** – saving and loading the movie data and similarity matrix
- **TMDb API** – movie information, posters, ratings, genres, and trailers

## 🔍 How It Works

The project uses a content-based recommendation approach.

1. The TMDB 5000 Movies and Credits datasets are loaded using Pandas.
2. The datasets are merged using the movie title.
3. Important movie features such as overview, genres, keywords, cast, and crew are selected.
4. The movie information is cleaned and combined into a `tags` column.
5. Movie tags are converted into numerical vectors using `CountVectorizer`.
6. Cosine Similarity is used to calculate similarity between movies.
7. The similarity matrix and processed movie data are saved using Pickle.
8. The Streamlit application loads these files and finds the top 5 similar movies.
9. The TMDb API is used to fetch additional movie details and trailers.

## 📂 Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── movies-recommender-system.ipynb
├── movie_list.pkl
├── similarity.pkl
├── output1.png
├── output2.png
├── output3.png
├── output4.png
└── README.md
