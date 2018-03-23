import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

_dbEngine = sqlalchemy.create_engine("sqlite:///database", echo=False)
_TableBase = declarative_base()
_Session = sessionmaker(bind=_dbEngine)()


class ExerciseType(_TableBase):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    @staticmethod
    def Count(name):
        return _Session.query(ExerciseType).filter(ExerciseType.name == name.lower()).count()

    @staticmethod
    def Post(name):
        exercise = ExerciseType.NullObject()
        if ExerciseType.Count(name) == 0:
            exercise = ExerciseType(name=name.lower())
            _Session.add(exercise)
            _Session.commit()
        else:
            exercise = ExerciseType.GetByName(name)
        return exercise

    @staticmethod
    def GetByName(name):
        try:
            query = _Session.query(ExerciseType).filter(ExerciseType.name == name.lower())
            ex = query.first()
            return ex
        except:
            return ExerciseType.NullObject()

    @staticmethod
    def GetAll():
        try:
            exercises = _Session.query(ExerciseType).all()
            return exercises
        except:
            return []

    @staticmethod
    def NullObject():
        return ExerciseType()


_TableBase.metadata.create_all(_dbEngine)
