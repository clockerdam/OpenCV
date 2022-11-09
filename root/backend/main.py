import json

from bson import json_util
from flask import Flask, request, Response, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from

from flask_cors import CORS

from api_specs import *
from prediction import improve_cv
from persistence import Connection as Database


app = Flask(__name__)
CORS(app)
swagger = Swagger(app)
db = Database()

@app.route("/")
def main():
    print("hello response")
    return "Hello World"

@app.post('/analysis')
@swag_from(analyze_resume_spec)
def analyze_resume():
    """Analyze resume and receive an improved version of it"""
    # Input: unlabeled resume
    # User input is saved in DB
    # Input is passed to model, model returns CV in shortened format.
    # Return: CV in shortened format

    payload = request.get_json()
    return improve_cv(payload)


@app.get('/labeled')
@swag_from(get_all_labeled_resumes_spec)
def get_all_labeled_resumes():
    """Endpoint returning a list of all labeled resumes stored in the database"""
    resumes = db.fetch_all_labeled_resumes()
    return Response(json_util.dumps(resumes),  mimetype='application/json')


@app.post('/label')
def label_unlabeled_resume():
    # ID used to remove unlabeled CV from the unlabeled cv collection

    # Insert labeled cv

    """Endpoint returning a list of all labeled resumes stored in the database"""
    resumes = db.fetch_all_labeled_resumes()
    return Response(json_util.dumps(resumes),  mimetype='application/json')

@app.post('/labeled')
@swag_from(upload_labeled_resume_spec)
def upload_labeled_resume():
    """Post labeled resume to the database"""
    payload = request.get_json()
    is_success = db.insert_labeled_resume(payload)
    if is_success:
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=400, mimetype='application/json')


@app.post('/unlabeled')
@swag_from(upload_unlabeled_resume_spec)
def upload_unlabeled_resume():
    """Post unlabeled resume to the database"""

    payload = request.get_json()
    is_success = db.insert_unlabeled_resume(payload)
    if is_success:
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=400, mimetype='application/json')

@app.get('/unlabeled/all')
@swag_from(get_all_unlabeled_resumes_spec)
def get_all_unlabeled_resumes():
    """Endpoint returning a list of all unlabeled resumes stored in the database"""
    resumes = db.fetch_all_unlabeled_resumes()
    return Response(json_util.dumps(resumes),  mimetype='application/json')

@app.get('/unlabeled')
def get_unlabeled_resume():
    """Endpoint returning an unlabeled resume stored in the database"""
    resume = db.fetch_unlabeled_resume()
    return Response(json_util.dumps(resume),  mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
