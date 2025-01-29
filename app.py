from flask import Flask, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    
    # Return JSON response containing the GitHub URL, current datetime, and email
    respone_data = {
        "email": "omobolanlehazeezat@gmail.com", 
        "current_datetime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), 
        "gitHub_url": "https://github.com/simplicityf/hng_task1.git"
    }
    return jsonify(respone_data)


if __name__ == '__main__':
    app.run()