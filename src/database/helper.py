from bson import ObjectId
from database.mongo_db import collection
from database.items import Item


async def create_item(item_name, item_value, item_descp, item_image):
    item = Item(
        item_name=item_name,
        item_value=float(item_value),
        item_descp=item_descp,
        item_image=item_image,
    )

    result = await collection.insert_one(item.__dict__)
    return str(result.inserted_id)


async def delete_item(item_id):
    result = await collection.delete_one(
        {"_id": ObjectId(item_id)}
    )
    return result.deleted_count


async def edit_item(item_id, updated_fields):
    if "item_value" in updated_fields:
        updated_fields["item_value"] = float(updated_fields["item_value"])

    result = await collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": updated_fields}
    )
    return result.modified_count


async def fetch_items(search=None, sort=None):
    query = {}

    if search:
        query["item_name"] = {
            "$regex": search,
            "$options": "i"
        }

    cursor = collection.find(query)

    if sort == "low":
        cursor = cursor.sort("item_value", 1)
    elif sort == "high":
        cursor = cursor.sort("item_value", -1)

    items = []
    async for item in cursor:
        item["_id"] = str(item["_id"])
        items.append(item)

    return items


async def add_cart_item(user_id, item_id):
    await collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$addToSet": {"cart_users": user_id}}
    )


async def remove_cart_item(user_id, item_id):
    await collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$pull": {"cart_users": user_id}}
    )


async def get_cart(user_id):
    cursor = collection.find(
        {"cart_users": user_id}
    )

    items = []
    total = 0

    async for item in cursor:
        item["_id"] = str(item["_id"])
        total += float(item["item_value"])
        items.append(item)

    return items, total


async def authenticate_user(email, password):
    if email == "demo@drift.com" and password == "password":
        return {"email": email}
    return None
