import json

from dotenv import dotenv_values
from pydantic import ValidationError
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from persistence.models.resume import Resume
from persistence.models.labeled_resume import Resume as LabeledResume
from bson import json_util

config = dotenv_values(".env")

class Connection:

    def __init__(self) -> None:
        super().__init__()
        self.labeled_resume_collection = None
        self.unlabeled_resume_collection = None
        self.database = None
        self.mongodb_client = None
        self.server_api = None
        self.db = None
        self.establish_connection()

    def establish_connection(self):
        self.mongodb_client = MongoClient(config["ATLAS_URI"])
        self.database = self.mongodb_client[
            config["DB"]]  
        self.server_api = ServerApi('1')
        self.labeled_resume_collection = self.database[config["LABELED_RESUME_COLLECTION"]]
        self.unlabeled_resume_collection = self.database[config["UNLABELED_RESUME_COLLECTION"]]
        print("Connected to DB")

    def shutdown_connection(self):
        self.mongodb_client.close()
        print("Connection to DB closed")

    def fetch_all_unlabeled_resumes(self):
        resumes = self.unlabeled_resume_collection.find({})
        try:
            map(Resume.parse_obj, resumes)
        except ValidationError as e:
            print(e)

        result = list(resumes)
        return result

    def fetch_all_labeled_resumes(self):
        resumes = self.labeled_resume_collection.find({})
        try:
            map(LabeledResume.parse_obj, resumes)
        except ValidationError as e:
            print(e)

        result = list(resumes)
        return result

    def insert_labeled_resume_from_file(self, filename: str):
        f = open(filename)
        my_dict = json.load(f)
        self.insert_labeled_resume(my_dict)

    def insert_unlabeled_resume_from_file(self, filename: str):
        f = open(filename)
        my_dict = json.load(f)
        self.insert_unlabeled_resume(my_dict)

    def insert_labeled_resume(self, resume: dict):
        written = False
        if Resume.parse_obj(resume):
            self.labeled_resume_collection.insert_one(resume)
        written = True
        return written

    def insert_unlabeled_resume(self, resume: dict):
        written = False
        if Resume.parse_obj(resume):
            self.unlabeled_resume_collection.insert_one(resume)
            written = True
        return written

