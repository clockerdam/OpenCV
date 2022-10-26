import flask
from flask_cors import CORS
from prediction import improve_cv


app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def main():
    print("hello response")
    return "Hello World"


@app.post("/labeledupload")
def labeledupload():
    print("labeledupload response")
    return "labeledupload"


@app.post("/cvupload")
def cvupload():
    return improve_cv()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
