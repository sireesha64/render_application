'''
from fastapi import FastAPI
from app.similarity import recommend_posts

app = FastAPI()

# -------------------- Home Route --------------------
@app.get("/")
def home():
    return {"message": "Social Feed Recommendation API is running"}

# -------------------- Recommendation Route --------------------
@app.get("/feed/{user_id}")
def get_feed(user_id: int):
    try:
        recommended = recommend_posts(user_id)

        return {
            "status": "success",
            "user_id": user_id,
            "recommended_posts": recommended
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
'''

import pickle
from fastapi import FastAPI
from models.recommender import FeedRecommender

app = FastAPI()

similarity = pickle.load(open("saved_models/similarity.pkl", "rb"))
interaction = pickle.load(open("saved_models/interaction.pkl", "rb"))
posts = pickle.load(open("saved_models/posts.pkl", "rb"))

recommender = FeedRecommender(similarity, interaction, posts)

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    return recommender.recommend(user_id)

