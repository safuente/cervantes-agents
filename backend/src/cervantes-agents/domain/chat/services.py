from .entities import Conversation, Message
from .value_objects import MessageRole
from typing import Protocol, List, Dict


class LLMClient(Protocol):
    def chat(self, messages: List[Dict], temperature: float) -> str:
        ...


def chat_with_character(conversation: Conversation, user_message: str, llm_client: LLMClient) -> str:
    conversation.history.append(Message(role=MessageRole.USER, content=user_message))

    messages = [{"role": m.role.value, "content": m.content} for m in conversation.history]
    response = llm_client.chat(messages, temperature=0.7)

    conversation.history.append(Message(role=MessageRole.ASSISTANT, content=response))
    return response