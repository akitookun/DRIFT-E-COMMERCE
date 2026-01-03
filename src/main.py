from database.mongo_db import collection
import asyncio


async def run():
    print(f"Collection obtained: {collection.name}")


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()
