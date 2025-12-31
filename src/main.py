from database.mongo_db import MongoDB
from pymongo.database import Collection


def main():
    db = MongoDB()
    collection: Collection = db.get_collection()
    print(f"Collection obtained: {collection.name}")


if __name__ == "__main__":
    main()
