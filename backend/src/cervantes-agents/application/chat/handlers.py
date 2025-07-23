from domain.chat.entities import Character, Conversation, Message
from domain.chat.value_objects import MessageRole
from domain.chat.services import chat_with_character
from infrastructure.llm.openai_client import OpenAIClient
from infrastructure.memory.mongo_memory_store import MongoMemoryStore

class ChatApplicationService:
    def __init__(self, llm_client=None, memory_store=None):
        self.llm_client = llm_client or OpenAIClient()
        self.memory_store = memory_store or MongoMemoryStore()

    async def handle_chat(self, session_id: str, character_id: str, user_message: str) -> str:
        characters = {
            "goya": Character(
                id="goya",
                name="Goya",
                persona="Eres Francisco de Goya, un pintor español del siglo XVIII...",
                description="Pintor de la corte y de lo grotesco"
            )
        }

        if character_id not in characters:
            raise ValueError("Personaje no encontrado")

        character = characters[character_id]

        history_docs = await self.memory_store.get_recent_messages(session_id)
        history = [
            Message(role=MessageRole(doc["role"]), content=doc["content"])
            for doc in history_docs
        ]
        history.append(Message(role=MessageRole.USER, content=user_message))

        conversation = Conversation(
            character=character,
            history=[Message(role=MessageRole.SYSTEM, content=character.persona)] + history
        )

        response = chat_with_character(conversation, user_message, self.llm_client)

        await self.memory_store.save_message(session_id, "user", user_message)
        await self.memory_store.save_message(session_id, "assistant", response)

        return response