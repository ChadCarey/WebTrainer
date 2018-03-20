import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

_dbEngine = sqlalchemy.create_engine("sqlite:///memory:", echo=True)
_TableBase = declarative_base()
Database = sessionmaker(bind=_dbEngine)()


class ExerciseType(_TableBase):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)


_TableBase.metadata.create_all(_dbEngine)
