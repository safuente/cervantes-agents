from motor.motor_asyncio import AsyncIOMotorClient
import os

class MongoMemoryStore:
    def __init__(self):
        mongo_url = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = AsyncIOMotorClient(mongo_url)
        self.db = self.client["cervantes_agents"]
        self.collection = self.db["short_term_memory"]

    async def save_message(self, session_id: str, role: str, content: str):
        await self.collection.insert_one({
            "session_id": session_id,
            "role": role,
            "content": content
        })

    async def get_recent_messages(self, session_id: str, limit: int = 10):
        cursor = self.collection.find({"session_id": session_id}).sort("_id", -1).limit(limit)
        results = await cursor.to_list(length=limit)
        return list(reversed(results))
