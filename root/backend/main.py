import json

from bson import json_util
from flask import Flask, request, Response
from flasgger import Swagger
from flasgger.utils import swag_from

from api_specs import *
from prediction import improve_cv
from persistence import Connection as Database

app = Flask(__name__)
swagger = Swagger(app)
db = Database()

@app.route('/')
def main():
    print("hello response")
    return 'Hello World'


@app.post('/labeled')
@swag_from(upload_labeled_resume_spec)
def upload_labeled_resume():
    """Post labeled resume to the database"""

    print("labeledupload response")
    return 'labeledupload'


@app.post('/analysis')
@swag_from(analyze_resume_spec)
def analyze_resume():
    """Analyze resume and receive an improved version of it"""

    payload = request.get_json()
    return improve_cv(payload)


@app.post('/unlabeled')
@swag_from(upload_unlabeled_resume_spec)
def upload_unlabeled_resume():
    """Post unlabeled resume to the database"""

    payload = request.get_json()
    is_success = db.insert_one_resume(payload)
    if is_success:
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=400, mimetype='application/json')


@app.get('/unlabeled')
@swag_from(get_all_unlabeled_resumes_spec)
def get_all_unlabeled_resumes():
    """Endpoint returning a list of all unlabeled resumes stored in the database"""
    return json_util.dumps(db.fetch_all_resumes())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
