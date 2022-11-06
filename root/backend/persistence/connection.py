import json

from dotenv import dotenv_values
from pydantic import ValidationError
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from .models import Resume

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
            config["DEV_DB"]]  # CHANGE TO PROD_DB to work with only valid data. # CHANGE TO DEV_DB for developing
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
            map(Resume.parse_obj, resumes)
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
        # if Resume.parse_obj(resume):
        print(type(resume))
        self.labeled_resume_collection.insert_one(resume)
        written = True
        return written

    def insert_unlabeled_resume(self, resume: dict):
        written = False
        if Resume.parse_obj(resume):
            self.unlabeled_resume_collection.insert_one(resume)
            written = True
        return written

db = Connection()
resumes = db.fetch_all_labeled_resumes()
'''db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS2.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS1.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS3.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS4.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS5.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS6.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS7.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS8.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS9.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/DS10.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE1.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE2.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE3.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE4.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE5.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE6.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE7.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE8.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE9.json")
db.insert_unlabeled_resume_from_file("root/backend/persistence/data/SE10.json")'''
db.shutdown_connection()


