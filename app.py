from flask import Flask, jsonify, request
import datetime
from flask_cors import CORS
from functions import get_fun_fact, is_armstrong, is_prime, is_perfect
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number')
def home():
    query = request.args.get('number')
    
    # Return an error if query is not pass or query is an alphabet
    if query is None or not query.isnumeric():
        return jsonify(number="alphabet", error="true"), 400
    else:
        num = int(query)
        properties = []
        
        if is_armstrong(num):
            properties.append("armstrong")
        properties.append("odd" if num % 2 != 0 else "even")
        
        result = {"number": num,
                  "is_prime": is_prime(num),
                  "is_perfect": is_perfect(num),
                  "properties": properties,
                  "digit_sum": sum(int(digit) for digit in str(num)),
                  "fun_fact": get_fun_fact(num),
            }
       
        return app.response_class(
            response=json.dumps(result, indent=4, sort_keys=False),  # Prevent sorting
            status=200,
            mimetype="application/json"
            )

if __name__ == '__main__':
    app.run()