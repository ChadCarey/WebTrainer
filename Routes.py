from flask import Flask, request
from Database.ExerciseType import ExerciseType
import Utils
app = Flask("TrainerAPI")


@app.route("/workout_type", methods=['POST', 'GET', ])
def addWorkoutType():
    if request.method == 'POST':
        name = request.form['name']
        exercise = ExerciseType.Post(name=name)
        return exercise.json
    elif request.method == "GET":
        return Utils.ToJson(ExerciseType.GetAll())


def Serve():
    app.run()

if __name__ == '__main__':
    Serve()
