from core.services import SVC
from sqlmodel import select, delete, update
from core.config import get_session
from .models import Hero


class HeroService(SVC):

    def _get_hero_id(self):  # helper method formatting
        pass

    def _get_hero_count(self):
        pass

    @classmethod
    def read(self, *args, **kwargs):
        heroes = get_session().exec(select(Hero)).all()
        return heroes

    @classmethod
    def write(self, *args, **kwargs):
        pk = kwargs["pk"] if "pk" in kwargs else None
        
        if not pk:
            pass
        else:
            session = get_session()
            db = session.get(Hero, pk)
            if db:
                hero = kwargs["hero"] if "hero" in kwargs else None
                data = hero.model_dump(exclude_unset=True)
                db.sqlmodel_update(data)
                session.add(db)
                session.commit()
                session.refresh(db)
                return db

    @classmethod
    def create(self, *args, **kwargs):
        hero = kwargs["hero"] if "hero" in kwargs else None
        if not hero:
            # raise exception
            pass
        else:
            session = get_session()
            hero = Hero(name=hero.name, active=True)
            session.add(hero)
            session.commit()
            session.refresh(hero)
            return hero

    @classmethod
    def unlink(self, *args, **kwargs):
        pk = kwargs["pk"] if "pk" in kwargs else None
        pass
