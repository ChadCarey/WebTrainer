from flask import Flask, request
from Database.ExerciseType import ExerciseType
import Utils
app = Flask("TrainerAPI")


@app.route("/workout_type", methods=['POST', 'GET', 'DELETE'])
def addWorkoutTypeRoute():
    if request.method == 'POST':
        name = request.form['name']
        exercise = ExerciseType.Post(name=name)
        return exercise.json
    elif request.method == "GET":
        return Utils.ToJson(ExerciseType.GetAll())
    elif request.method == "DELETE":
        name = request.form['name']
        return ExerciseType.DeleteByName(name)


def Serve():
    app.run()

if __name__ == '__main__':
    Serve()
