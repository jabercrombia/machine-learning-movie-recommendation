from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from difflib import get_close_matches


# Prepare data
movies = pd.read_csv('src/movies.csv')
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Init FastAPI
app = FastAPI()

# Enable CORS for your Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this to match your frontend's origin
    allow_methods=["*"],
    allow_headers=["*"],
)

indices = pd.Series(movies.index, index=movies['title'].str.lower()).drop_duplicates()


@app.get("/recommend")
def recommend(title: str = Query(...), num_recommendations: int = 5):
    title = title.lower().strip()

    if title not in indices:
        # Try to find closest match
        close_matches = get_close_matches(title, indices.index, n=1, cutoff=0.6)
        if not close_matches:
            return {"error": "Movie not found"}
        title = close_matches[0]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    recs = movies.iloc[movie_indices][['title', 'genres']].to_dict(orient="records")
    return {"recommendations": recs}
