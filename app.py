from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(email="omobolanlehazeezat@gmail.com", date=datetime)