from dataclasses import dataclass

@dataclass
class Character:
    id: str            # unique identifier, e.g. "goya"
    name: str          # full name, e.g. "Francisco de Goya"
    persona: str       # system prompt defining personality
    description: str   # short description used in listings
