from sqlalchemy import Column, Integer, String, Date
from Database import TableBase, Session
import json

class ExerciseType(TableBase):
    __tablename__ = "exercise_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    @property
    def json(self):
        return json.dumps({
                'data_type': self.__class__.__name__,
                'id': self.id,
                'name': self.name
            })

    @staticmethod
    def Count(name):
        return Session.query(ExerciseType).filter(ExerciseType.name == name.lower()).count()

    @staticmethod
    def Post(name):
        exercise = ExerciseType.NullObject()
        if ExerciseType.Count(name) == 0:
            exercise = ExerciseType(name=name.lower())
            Session.add(exercise)
            Session.commit()
        else:
            exercise = ExerciseType.GetByName(name)
        return exercise

    @staticmethod
    def GetByName(name):
        try:
            query = Session.query(ExerciseType).filter(ExerciseType.name == name.lower())
            ex = query.first()
            return ex
        except:
            return ExerciseType.NullObject()

    @staticmethod
    def GetAll():
        try:
            exercises = Session.query(ExerciseType).all()
            return exercises
        except:
            return []

    @staticmethod
    def NullObject():
        return ExerciseType()
