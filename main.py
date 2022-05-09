from flask import Flask, request, jsonify
from database import Database

db = Database()
app = Flask(__name__)
print(__name__)


@app.route("/api/auth", methods=["POST"])
def sign_in():
    pass


@app.route("/api/auth", methods=["DELETE"])
def sign_out():
    pass


@app.route("/api/users", methods=["GET"])
def get_users():
    if len(db.data) == 0:
        return "", 204
    return jsonify(db.data), 200


@app.route("/api/users", methods=["POST"])
def sign_up():
    if {"email", "password", "name"} <= request.json.keys():
        email = request.json["email"]
        password = request.json["password"]
        name = request.json["name"]
    else:
        return "", 400

    if db.find_by_email(email) is not None:
        return "", 409
    db.create(email, password, name)
    return "", 201


@app.route("/api/users/current", methods=["GET"])
def get_current():
    pass


@app.route("/api/users/current", methods=["DELETE"])
def remove_current():
    pass
