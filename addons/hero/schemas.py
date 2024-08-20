from sqlmodel import Field
from core.models import Model


class HeroCreate(Model):
    name: str = Field(index=True)
