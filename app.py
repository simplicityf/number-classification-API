from flask import Flask, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    
    # Return JSON response containing the GitHub URL, current datetime, and email
    return jsonify(GitHub_url="https://github.com/simplicityf/hng_task1.git", current_datetime=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), email="omobolanlehazeezat@gmail.com")


if __name__ == '__main__':
    app.run()