from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return {
        "slackUsername": "promisee",
        "backend": True,
        "age": 18,
        "bio": "a tech enthusiast"
    }

if __name__ == '__main__':
    app.run(debug=True)