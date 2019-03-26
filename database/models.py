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

    def __str__(self):
        return str(self.id).ljust(3) + str(self.name).ljust(20) + str(round(self.price/100, 2)).ljust(10) + str(self.description).ljust(30)