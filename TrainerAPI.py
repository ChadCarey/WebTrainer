from flask import Flask, request
app = Flask("TrainerAPI")


@app.route("/workout_type", methods=['POST','GET',])
def addWorkoutType():
    if request.method == 'POST':
        postWorkoutType()
    elif request.method == "GET":
        return getWorkoutTypes()

if __name__ == '__main__':
    app.run()
