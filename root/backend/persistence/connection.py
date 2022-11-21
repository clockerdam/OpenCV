import json

from bson import ObjectId
from dotenv import dotenv_values
from pydantic import ValidationError
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from .models import Resume, IdentifiableResume

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


    def fetch_unlabeled_resume(self):
        resume = self.unlabeled_resume_collection.find_one()
        try:
            map(Resume.parse_obj, resume)
        except ValidationError as e:
            print(e)

        return resume


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

        print(resume['_id'])
        print(type(resume['_id']['$oid']))
        resume['_id'] = ObjectId(resume['_id']['$oid'])
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


    def delete_unlabeled_resume(self, resume_id: str):
        query = {"_id": ObjectId(resume_id)}

        found = self.unlabeled_resume_collection.find_one(query)
        if found is None:
            raise KeyError("No unlabeled resume with this id found")

        deleted = self.unlabeled_resume_collection.delete_one(query)
        return deleted



# db = Connection()
# resumes = db.fetch_all_labeled_resumes()
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS1.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS2.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS3.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS4.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS5.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS6.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS7.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS8.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS9.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_DS10.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE1.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE2.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE3.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE4.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE5.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE6.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE7.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE8.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE9.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_SE10.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA1.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA2.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA3.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA4.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA5.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA6.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA7.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA8.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA9.json")
# db.insert_unlabeled_resume_from_file("root/backend/persistence/data/l_BA10.json")
######### LABELED
#db.insert_labeled_resume_from_file("root/backend/persistence/data/labeled_DS9.json")


