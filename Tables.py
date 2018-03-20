import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

dbEngine = sqlalchemy.create_engine("sqlite:///memory:", echo=True)
TableBase = declarative_base()

class ExerciseType(TableBase):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    type_name = Column(String)

