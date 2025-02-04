from flask import Flask, jsonify, request
from flask_cors import CORS
from functions import get_fun_fact, is_armstrong, is_prime, is_perfect
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number')
def home():
    query = request.args.get('number')
    
    # Return an error if query is not pass or query is an alphabet
    if query is None or not query.lstrip('-').isdigit():
        result = {
            "number": "alphabet",
            "error": True
        }
        return app.response_class(
            response=json.dumps(result, indent=4, sort_keys=False),  # Prevent sorting
            status=400,
            mimetype="application/json"
            )
    else:
        num = int(query)
        properties = []
        
         # Handle Armstrong numbers (usually for non-negative numbers)
        if num >= 0 and is_armstrong(num):
            properties.append("armstrong")
        
        # Check for odd/even properties
        properties.append("odd" if num % 2 != 0 else "even")
        
        # Calculate digit sum (should be negative for negative numbers)
        digit_sum = sum(int(digit) for digit in str(abs(num)))  # Get sum of digits
        if num < 0:
            digit_sum *= -1
        
        result = {"number": num,
                  "is_prime": is_prime(num),
                  "is_perfect": is_perfect(num),
                  "properties": properties,
                  "digit_sum": digit_sum,
                  "fun_fact": get_fun_fact(num),
            }
       
        return app.response_class(
            response=json.dumps(result, indent=4, sort_keys=False),  # Prevent sorting
            status=200,
            mimetype="application/json"
            )

if __name__ == '__main__':
    app.run()