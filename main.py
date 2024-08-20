from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import initialize
from addons.hero.models import Hero
from addons.hero.routes import router as hero_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(hero_route)


# import routes
# TODO: look for auto import routes
# from addons.hero.routes import heroes
