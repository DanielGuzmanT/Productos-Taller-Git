from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id          = Column(Integer, primary_key=True)
    name        = Column(String(200))
    price       = Column(Integer)
    description = Column(String(300))

    def __repr__(self):
        return "<Product(id='{}', name='{}', price='{}', description='{}')>"\
        .format(self.id, self.name, self.price/10, self.description)
