from .db_connector import engine
from .models_orm import Base

Base.metadata.create_all(engine)
