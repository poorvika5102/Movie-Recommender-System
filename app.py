import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import RequestException

# Setup requests session with retry
session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Function to fetch movie poster, details, and trailer
def fetch_movie_details(movie_id):
    try:
        # Fetch movie metadata
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = session.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Fetch trailer video
        video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        video_response = session.get(video_url, timeout=10)
        video_response.raise_for_status()
        video_data = video_response.json()

        trailer_key = ""
        for video in video_data.get('results', []):
            if video['type'] == "Trailer" and video['site'] == "YouTube":
                trailer_key = video['key']
                break

        trailer_url = f"https://www.youtube.com/embed/{trailer_key}" if trailer_key else None

        poster_path = data.get('poster_path', '')
        full_poster_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

        movie_info = {
            "title": data.get('title', 'Unknown'),
            "overview": data.get('overview', 'No description available.'),
            "rating": data.get('vote_average', 'N/A'),
            "genres": ", ".join([genre['name'] for genre in data.get('genres', [])]),
            "trailer_url": trailer_url
        }

        return full_poster_path, movie_info

    except RequestException as e:
        st.error("⚠️ Could not fetch movie details due to a connection issue. Please try again later.")
        print(f"[ERROR] {e}")
        return "", {
            "title": "Unavailable",
            "overview": "Movie information could not be loaded.",
            "rating": "N/A",
            "genres": "N/A",
            "trailer_url": None
        }

# Function to get recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in distances[1:6]:  # Top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        poster, details = fetch_movie_details(movie_id)
        recommended_movies.append({"poster": poster, "details": details})

    return recommended_movies

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("Get personalized movie recommendations based on your favorite movie! 🍿")

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selector
selected_movie = st.selectbox("🔍 Search or select a movie:", movies['title'].values)

# Show recommendations
if st.button("🎥 Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        recommended_movies = recommend(selected_movie)

    st.markdown("## 📌 Recommended Movies")
    cols = st.columns(len(recommended_movies))

    for col, movie in zip(cols, recommended_movies):
        with col:
            st.image(movie["poster"], use_column_width=True)
            st.markdown(f"🎬 {movie['details']['title']}")
            st.markdown(f"⭐ Rating: {movie['details']['rating']}")
            st.markdown(f"🎭 Genres: {movie['details']['genres']}")

            with st.expander(f"📖 Read more about {movie['details']['title']}"):
                st.markdown(
                    f"<div style='text-align: justify;'>{movie['details']['overview']}</div>",
                    unsafe_allow_html=True
                )
                if movie["details"]["trailer_url"]:
                    st.markdown("🎬 *Watch Trailer:*")
                    st.video(movie["details"]["trailer_url"])