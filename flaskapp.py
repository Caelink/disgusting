from flask import Flask, jsonify

app = Flask(__name__)

opinions = {"marth":"disgusting"}

@app.route('/')
def index():
    return "Welcome to the memes!"

@app.route('/api/opinion')
def opinion():
    return jsonify({"opinions": opinions})

if __name__ == '__main__':
    app.run(debug=True)

