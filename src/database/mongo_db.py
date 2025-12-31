from pymongo import AsyncMongoClient
from pymongo.database import Database, Collection
from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")


class MongoDB:
    def __init__(self):
        self.client: AsyncMongoClient = AsyncMongoClient(MONGO_URI)
        self.db: Database = self.client["drift_ecommerce_db"]

    def get_collection(self) -> Collection:
        return self.db.get_collection("inventory")
