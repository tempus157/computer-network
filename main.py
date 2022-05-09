from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route("/api/auth", methods=["POST"])
def sign_in():
    pass


@app.route("/api/auth", methods=["DELETE"])
def sign_out():
    pass


@app.route("/api/users", methods=["POST"])
def sign_up():
    pass


@app.route("/api/users/current", methods=["GET"])
def get_current():
    pass


@app.route("/api/users/current", methods=["DELETE"])
def remove_current():
    pass
