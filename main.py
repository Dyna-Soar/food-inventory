import fastapi

from sqlalchemy import create_engine

import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

engine = create_engine("sqlite:///"+os.path.join(BASE_DIR, "database.db"), echo=True, future=True)


# Read table

# Create row

# Update row

# Delete row
