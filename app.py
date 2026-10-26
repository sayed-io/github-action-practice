# This code is from the github repo https://github.com/LondheShubham153/flask-app-ecs.git
# Made some changes in the code AND RUN
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/health")
def health():
    return "Server is up and running"
