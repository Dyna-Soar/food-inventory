from .db_connector import engine, Session
from .models_orm import Food


class ReadFoods:
    def __init__(self):
        local_session = Session(bind=engine)
        self.foods = local_session.query(Food).all()


class ReadFood:
    def __init__(self, id):
        local_session = Session(bind=engine)
        self.food = local_session.get(Food, id)
