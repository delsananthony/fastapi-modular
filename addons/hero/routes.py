from fastapi import APIRouter
from .models import Hero
from .schemas import HeroCreate
from .services import HeroService

router = APIRouter(prefix="/hero", tags=["hero"])


@router.get("/", response_model=list[Hero])
def get_heroes():
    return HeroService.read()


@router.post("/", response_model=Hero)
def create_hero(hero: HeroCreate):
    return HeroService.create(hero=hero)


@router.patch("/{pk}", response_model=Hero)
def write_hero(pk: int, hero: HeroCreate):
    return HeroService.write(hero=hero, pk=pk)
