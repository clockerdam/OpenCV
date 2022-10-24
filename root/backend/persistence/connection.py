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
        self.resume_collection = self.database.resumes
        print("Connected to the MongoDB database!")

    def load_one_json(self, filename):
        collection = self.resume_collection
        f = open(filename)
        my_dict = json.load(f)
        print(my_dict)
        result = collection.insert_one(my_dict)
        print(result)

    def shutdown_connection(self):
        self.mongodb_client.close()


db = Connection()
db.load_one_json("DS2.json")
db.shutdown_connection()