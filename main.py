from flask import Flask, request, jsonify
from database import Database
import bcrypt
import jwt

secret = "N34T&h*^fF=8F!PU2zctu@q^fr_9C&WE"
db = Database()
app = Flask(__name__)


@app.route("/api/auth", methods=["POST"])
def sign_in():
    if {"email", "password"} <= request.json.keys():
        email = request.json["email"]
        password = request.json["password"]
    else:
        return "", 400

    user = db.find_by_email(email)
    if user is None:
        return "", 404
    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return "", 404

    credential = {"credential": jwt.encode({"email": user["email"]}, secret)}
    return jsonify(credential), 201


@app.route("/api/auth", methods=["DELETE"])
def sign_out():
    credential = request.headers.get("Authorization")
    if credential is None:
        return "", 400

    credential = credential.replace("Bearer ", "")
    user = db.find_by_credential(credential, secret)
    return "", 200 if user is not None else 401


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
    db.print()
    return "", 201


@app.route("/api/users/current", methods=["GET"])
def get_current():
    pass


@app.route("/api/users/current", methods=["DELETE"])
def remove_current():
    pass
