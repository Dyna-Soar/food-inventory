from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

engine = create_engine("sqlite:///"+os.path.join(BASE_DIR, "database.db"), echo=True, future=True)

Session = sessionmaker()
