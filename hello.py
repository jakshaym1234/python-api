from flask import Flask,jsonify
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/dog")
def hello_dog():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    return jsonify(response.text)

@app.route("/cat")
def hello_cat():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    return jsonify(response.text)