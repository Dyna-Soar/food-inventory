from db_connector import engine, Session
from models_orm import Food


class DeleteFood:
    def __init__(self, food_id):
        local_session = Session(bind=engine)
        food_to_delete = local_session.get(Food, food_id)
        local_session.delete(food_to_delete)
        local_session.commit()
