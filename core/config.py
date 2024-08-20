# database and backend config
from sqlmodel import SQLModel, Session, create_engine, select
import logging

_logger = logging.getLogger("SQLModel Initialize")

sqlite_file_name = "Hero.db"

DB_TEMPLATE = {
    "DB_URL": f"sqlite:///{sqlite_file_name}",
}

connect_args = {"check_same_thread": False}
engine = create_engine(DB_TEMPLATE["DB_URL"], echo=True, connect_args=connect_args)


def initialize():
    _logger.info("****Creating Tables****")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        return session
