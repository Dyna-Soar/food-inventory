from main import engine
from models_orm import Base

Base.metadata.create_all(engine)
