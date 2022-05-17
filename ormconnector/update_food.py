from fastapi.encoders import jsonable_encoder

from .db_connector import engine, Session
from .models_orm import Food


class UpdateFoodAmount:
    def __init__(self, food_id, amount):
        local_session = Session(bind=engine)
        food_to_update = local_session.get(Food, food_id)
        food_to_update.amount = amount
        local_session.commit()
        self.update_food = jsonable_encoder(local_session.get(Food, food_id))


class UpdateFoodPrice:
    def __init__(self, food_id, price):
        local_session = Session(bind=engine)
        food_to_update = local_session.get(Food, food_id)
        food_to_update.price = price
        food_to_update.final_price = float(price) * (1 + float(food_to_update.vat))
        local_session.commit()
        self.update_food = jsonable_encoder(local_session.get(Food, food_id))


class UpdateFoodVat:
    def __init__(self, food_id, vat):
        local_session = Session(bind=engine)
        food_to_update = local_session.get(Food, food_id)
        food_to_update.vat = vat
        food_to_update.final_price = float(food_to_update.price) * (1 + float(vat))
        local_session.commit()
        self.update_food = local_session.get(Food, food_id)
