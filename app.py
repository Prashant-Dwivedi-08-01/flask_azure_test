from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import time

app = Flask(__name__)


users = [
    {"name": "John", "age": 32, "gender": "male"},
    {"name": "Jane", "age": 28, "gender": "female"},
    {"name": "Bob", "age": 45, "gender": "male"}
]

@app.route('/user', methods=["POST"])
def get_user_info():
    name = request.json.get("name")
    time.sleep(4)
    for user in users:
        if user["name"] == name:
            return jsonify(user)
    return jsonify({"message": "User not found"})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/welcome", methods=["POST"])
def welcome():
    try:
        name = request.json.get("name")
        return jsonify({"message": "Welcome, {}!".format(name)})
    except Exception as e:
        return jsonify({"message": "Welcome, World!. Somnething went wrong: {}".format(e)})
