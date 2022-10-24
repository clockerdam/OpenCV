# from dotenv import dotenv_values
from pymongo import MongoClient, InsertOne
from pymongo.server_api import ServerApi
import json

# config = dotenv_values(".env")
ATLAS_URI = "mongodb+srv://opencv:project4ds@cluster0.7jvzenl.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "OpenCV"
RESUME_COLLECTION = "resumes"


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
        self.mongodb_client = MongoClient(ATLAS_URI)
        self.database = self.mongodb_client[DB_NAME]
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
