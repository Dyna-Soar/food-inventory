from db_connector import engine, Session
from models_orm import Food


class CreateFood:
    def __init__(self, id, name, amount, price, vat, category):
        new_food = Food(
            id=id,
            name=name,
            amount=amount,
            price=price,
            vat=vat,
            category=category,
            final_price=float(price)*(1+float(vat))
        )
        local_session = Session(bind=engine)
        local_session.add(new_food)
        local_session.commit()
