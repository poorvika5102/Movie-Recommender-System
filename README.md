# 🎬 Movie Recommender System

A content-based Movie Recommender System built using **Python, Streamlit, and TMDb API**. The application recommends movies similar to a movie selected by the user and displays useful details such as posters, genres, ratings, overviews, and trailers.

## 🚀 Features

- 🎥 Select a movie and get the **Top 5 similar movies**
- 🖼️ Display movie posters and details
- ⭐ Show movie ratings
- 🎭 Display genres and movie overviews
- ▶️ Watch movie trailers directly from the app
- 🔎 Interactive movie selection
- 🌐 Fetch real-time movie details using the TMDb API
- ⚡ Responsive Streamlit interface
- 🛡️ Handles API and network errors gracefully

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Requests**
- **Pickle**
- **TMDb API**

## 🔍 How It Works

The project has two main components:

### 1. Movie Recommendation Model

The Jupyter Notebook `movies-recommender-system.ipynb` is used for data preprocessing and building the recommendation system.

The process includes:

- Loading and processing the movie dataset
- Preparing movie features
- Calculating similarity between movies using **Cosine Similarity**
- Saving the processed movie data and similarity matrix using Pickle

Generated files:

```text
movie_list.pkl
similarity.pkl
