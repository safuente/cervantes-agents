from domain.chat.entities import Conversation, Message
from domain.chat.value_objects import MessageRole
from domain.chat.services import chat_with_character
from domain.characters.historical_factory import HistoricalCharacterFactory
from infrastructure.llm.openai_client import OpenAIClient
from infrastructure.memory.mongo_memory_store import MongoMemoryStore


class ChatApplicationService:
    def __init__(self, llm_client=None, memory_store=None):
        self.llm_client = llm_client or OpenAIClient()
        self.memory_store = memory_store or MongoMemoryStore()

    async def handle_chat(self, session_id: str, character_id: str, user_message: str) -> str:
        # Get character
        character = HistoricalCharacterFactory.get_character(character_id)

        # Get short-term memory (past messages)
        past_messages = await self.memory_store.get_recent_messages(session_id)

        # Start conversation with persona as system prompt
        history = [Message(role=MessageRole.SYSTEM, content=character.persona)] + past_messages

        # Create conversation
        conversation = Conversation(character=character, history=history)

        # Chat
        response = chat_with_character(conversation, user_message, self.llm_client)

        # Store user + assistant messages in memory
        await self.memory_store.save_message(session_id, MessageRole.USER.value, user_message)
        await self.memory_store.save_message(session_id, MessageRole.ASSISTANT.value, response)

        return response
