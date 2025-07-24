from fastapi import FastAPI
from .routes import scripture_routes, saved_verses

app = FastAPI()

app.include_router(scripture_routes.router)
app.include_router(saved_verses.router)





# @app.get("/")
# def root():
#     return {"message": "Welcome to the Word Declaration App!"}

# @app.post("/get-scripture")
# def get_scripture(feeling: str):
#     verse = get_scripture_for_feeling(feeling)
#     return {"feeling": feeling, "verse": verse}s