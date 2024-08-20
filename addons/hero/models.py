from sqlmodel import Field
from core.models import Model


class Hero(Model, table=True):

    name: str = Field(index=True)
    active: bool = Field(default=False)
