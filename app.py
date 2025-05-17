from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient

app = Flask(__name__)

# Replace this with your actual MongoDB Atlas URI
client = MongoClient("mongodb+srv://rahul123:rahul123@cluster0.zagyrwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['flaskDB']
collection = db['submissions']

@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        try:
            collection.insert_one({"name": name, "age": age})
            return redirect(url_for("success"))
        except Exception as e:
            return render_template("form.html", error=str(e))
    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
