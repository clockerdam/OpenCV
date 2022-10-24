from dotenv import dotenv_values
from pymongo import MongoClient, InsertOne
from pymongo.server_api import ServerApi
import json

config = dotenv_values(".env")


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
        self.database = self.mongodb_client[config["DB_NAME"]]
        self.server_api = ServerApi('1')
        self.resume_collection = self.database[config["RESUME_COLLECTION"]]
        print("Connected to DB")

    def shutdown_connection(self):
        self.mongodb_client.close()
        print("Connection to DB closed")

    def fetch_all_resumes(self):
        return list(self.resume_collection.find({}))

    def insert_resume_from_file(self, filename: str):
        f = open(filename)
        my_dict = json.load(f)

        self.insert_resume(my_dict)

    def insert_one_resume(self, resume_json: dict):
        result = self.resume_collection.insert_one(resume_json)


db = Connection()
resumes = db.fetch_all_resumes()
print(resumes)
db.shutdown_connection()
