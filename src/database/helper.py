from database.mongo_db import collection
from database.items import Item
from pymongo.collection import ObjectId


async def create_item(item_name, item_value, item_descp, item_image):
    item = Item(
        item_name=item_name,
        item_value=item_value,
        item_descp=item_descp,
        item_image=item_image,
    )

    insert_id = await collection.insert_one(item.__dict__)

    return insert_id


async def delete_item(item_id):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count


async def edit_item(item_id, updated_fields):
    result = await collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": updated_fields}
    )
    return result.modified_count
