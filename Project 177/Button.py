from flask import Flask, render_template, jsonify, request
import random
app=Flask(__name__)
templates=[
    {
        "inputs":5,
        "category":"Sports",
        "word":"Chess"
    },
    {
        "inputs":6,
        "category":"European Country Name",
        "word":"France"
    }
]
@app.route("/")
def index():
    return render_template("Project 176.html")
@app.route("/get-story")
def get_story():
    return jsonify({
        "status": "success",
        "story": random.choice(templates)
    })