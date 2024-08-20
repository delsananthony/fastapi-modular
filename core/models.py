# abstract model format
from sqlmodel import Field, Session, SQLModel
from datetime import datetime


class BaseModel(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    create_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    write_date: datetime = Field(default_factory=datetime.utcnow, nullable=False)


AbstractModel = BaseModel


class Model(AbstractModel):
    pass


if __name__ == "__main__":
    pass
