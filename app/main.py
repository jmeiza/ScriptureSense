from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from fastapi import FastAPI
from .routes import scripture_routes, saved_verses
from .routes.auth import router as auth_router
from .models.database import Base, engine
from .models import saved_verse_model 


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(scripture_routes.router)
app.include_router(saved_verses.router, prefix="/saved-verses")
app.include_router(auth_router, prefix="/auth")

