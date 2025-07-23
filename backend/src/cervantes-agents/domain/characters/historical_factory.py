from domain.characters.entities import Character
from domain.characters.exceptions import (
    CharacterIdNotFound,
    CharacterPersonaNotFound,
    CharacterDescriptionNotFound,
)

CHARACTER_NAMES = {
    "goya": "Francisco de Goya",
    "cervantes": "Miguel de Cervantes",
    "isabel": "Isabella I of Castile",
}

CHARACTER_PERSONAS = {
    "goya": "You are Francisco de Goya, an 18th-century Spanish painter. Critical, melancholic, and dark.",
    "cervantes": "You are Miguel de Cervantes, author of Don Quixote. Witty, ironic, and deeply observant of human nature.",
    "isabel": "You are Isabella I of Castile, Queen of Spain. Strategic, devout, and focused on unity.",
}

CHARACTER_DESCRIPTIONS = {
    "goya": "Court painter and master of the grotesque.",
    "cervantes": "Pillar of Spanish literature and author of Don Quixote.",
    "isabel": "Key monarch in the unification of Spain.",
}

AVAILABLE_CHARACTERS = list(CHARACTER_NAMES.keys())


class HistoricalCharacterFactory:
    @staticmethod
    def get_character(character_id: str) -> Character:
        character_id = character_id.lower()

        if character_id not in CHARACTER_NAMES:
            raise CharacterIdNotFound(character_id)

        if character_id not in CHARACTER_PERSONAS:
            raise CharacterPersonaNotFound(character_id)

        if character_id not in CHARACTER_DESCRIPTIONS:
            raise CharacterDescriptionNotFound(character_id)

        return Character(
            id=character_id,
            name=CHARACTER_NAMES[character_id],
            persona=CHARACTER_PERSONAS[character_id],
            description=CHARACTER_DESCRIPTIONS[character_id],
        )

    @staticmethod
    def get_available_characters() -> list[str]:
        return AVAILABLE_CHARACTERS
