from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Float)
    vat = Column(Float)
    category = Column(String(30))
    final_price = Column(Float)
    amount = Column(Integer)

    def __repr__(self):
        return f"Food(id={self.id!r}, name={self.name!r}, category={self.category!r} final_price={self.final_price!r}, amount={self.amount!r})"
