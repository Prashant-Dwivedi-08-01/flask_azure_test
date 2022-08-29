from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

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