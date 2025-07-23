from dataclasses import dataclass
from typing import List
from .value_objects import MessageRole


@dataclass
class Message:
    role: MessageRole
    content: str


@dataclass
class Character:
    id: str
    name: str
    persona: str
    description: str


@dataclass
class Conversation:
    character: Character
    history: List[Message]