class CharacterIdNotFound(Exception):
    def __init__(self, character_id: str):
        super().__init__(f"Character ID '{character_id}' not found.")

class CharacterPersonaNotFound(Exception):
    def __init__(self, character_id: str):
        super().__init__(f"Persona for character '{character_id}' not found.")

class CharacterDescriptionNotFound(Exception):
    def __init__(self, character_id: str):
        super().__init__(f"Description for character '{character_id}' not found.")