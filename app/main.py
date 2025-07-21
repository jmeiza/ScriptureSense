from fastapi import FastAPI
from .matcher import get_scripture_for_feeling

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Word Declaration App!"}

@app.post("/get-scripture")
def get_scripture(feeling: str):
    verse = get_scripture_for_feeling(feeling)
    return {"feeling": feeling, "verse": verse}