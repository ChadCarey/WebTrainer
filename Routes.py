from flask import Flask, request
app = Flask("TrainerAPI")


@app.route("/workout_type", methods=['POST', 'GET', ])
def addWorkoutType():
    if request.method == 'POST':
        return "Post"
    elif request.method == "GET":
        return "Get"


def Serve():
    app.run()

if __name__ == '__main__':
    Serve()
