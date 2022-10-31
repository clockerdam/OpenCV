import json

from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from models.resume import Resume
from bson import json_util

config = dotenv_values("root/backend/.env")


class Connection:

    def __init__(self) -> None:
        super().__init__()
        self.resume_collection = None
        self.database = None
        self.mongodb_client = None
        self.server_api = None
        self.db = None
        self.establish_connection()

    def establish_connection(self):
        self.mongodb_client = MongoClient(config["ATLAS_URI"])
        self.database = self.mongodb_client[config["DEV_DB"]]
        self.server_api = ServerApi('1')
        self.resume_collection = self.database[config["RESUME_COLLECTION"]]
        print("Connected to DB")

    def shutdown_connection(self):
        self.mongodb_client.close()
        print("Connection to DB closed")

    def fetch_all_resumes(self):
        map(Resume.parse_obj, self.resume_collection.find({}))
        result = list(self.resume_collection.find({}))
        return json_util.dumps(result)

    def insert_resume_from_file(self, filename: str):
        f = open(filename)
        my_dict = json.load(f)
        self.insert_one_resume(my_dict)

    def insert_one_resume(self, resume: dict):
        written = False
        if Resume.parse_obj(resume):
            self.resume_collection.insert_one(resume)
            written = True
        return written
