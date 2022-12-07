import json
import os

from bson import json_util
from flask import Flask, request, Response, jsonify, send_from_directory
from flasgger import Swagger
from flasgger.utils import swag_from

from flask_cors import CORS

from api_specs import *
from prediction import improve_cv
from persistence import Connection as Database
from persistence.models import Resume

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3,
    'openapi': '3.0.2'
}
CORS(app)
swagger = Swagger(app)
db = Database()


@app.route("/")
def main():
    print("hello response")
    return "Hello World"


@app.route("/pdf")
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files/'
    return send_from_directory(filepath, 'sample_cv.pdf')


@app.post('/analysis')
@swag_from(analyze_resume_spec)
def analyze_resume():
    """Analyze resume and receive an improved version of it"""
    print("Analysing resume!")

    # Input: unlabeled resume
    # User input is saved in DB
    # Input is passed to model, model returns CV in shortened format.
    # Return: CV in shortened format
    payload = request.get_json()
    return improve_cv(payload)


@app.post('/label')
@swag_from(label_unlabeled_resume_spec)
def label_unlabeled_resume():
    """Label unlabeled resume"""
    # ID used to remove unlabeled CV from the unlabeled cv collection

    # Insert labeled cv
    resume = request.get_json()
    try:
        resume_id = resume['_id']['$oid']
    except:
        raise AttributeError("The given resume does not have an id attribute")

    labeled_resume = db.insert_labeled_resume(resume)
    db.delete_unlabeled_resume(resume_id)

    return Response(json_util.dumps(labeled_resume), mimetype='application/json')


@app.get('/labeled/all')
@swag_from(get_all_labeled_resumes_spec)
def get_all_labeled_resumes():
    """Endpoint returning a list of all labeled resumes stored in the database"""
    resumes = db.fetch_all_labeled_resumes()
    return Response(json_util.dumps(resumes), mimetype='application/json')


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
    return Response(json_util.dumps(resumes), mimetype='application/json')


@app.get('/unlabeled')
@swag_from(get_unlabeled_resume_spec)
def get_unlabeled_resume():
    """Endpoint returning an unlabeled resume stored in the database"""
    resume = db.fetch_unlabeled_resume()
    return Response(json_util.dumps(resume), mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
