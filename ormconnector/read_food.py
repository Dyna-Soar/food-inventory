from fastapi.encoders import jsonable_encoder
from .db_connector import engine, Session
from .models_orm import Food


class ReadFoods:
    def __init__(self):
        local_session = Session(bind=engine)
        self.foods = jsonable_encoder(local_session.query(Food).all())


class ReadFood:
    def __init__(self, id):
        local_session = Session(bind=engine)
        self.food = jsonable_encoder(local_session.get(Food, id))
