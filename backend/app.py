from flask import Flask, jsonify, request
from random import randint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# random num
random_number = randint(1, 100)

@app.route('/guess', methods=['POST'])
def guess():
    global random_number
    user_guess = request.json['number']
    if user_guess < random_number:
        return jsonify("Please guess larger"), 200
    elif user_guess > random_number:
        return jsonify("Please guess smaller"), 200
    else:
        random_number = randint(1, 100)  # reset
        return jsonify("Congratulations! You guessed it right."), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
