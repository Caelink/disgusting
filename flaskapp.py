from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

#globals
opinions = {"marth":"disgusting"}

@app.route('/api')
def index():
    return "Welcome to the memes!"

@app.route('/api/opinion')
def opinion():
    return jsonify({"opinions": opinions})

if __name__ == '__main__':
    app.run(debug=True)

