from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import database

Base = database.get_base()


class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer)
    time = Column(Integer)
    data = Column(String)

    class Config:
        orm_mode = True  # necessary for SQLAlchemy to map the models to ORM objects
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
