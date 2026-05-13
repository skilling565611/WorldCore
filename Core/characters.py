# characters.py
# Lightweight WorldCore character and AI-like entity registry.
# This is fictional data only and does not call real AI models or services.

characters = {
    "dev_operator": {
        "display_name": "Dev Operator",
        "character_type": "operator",
        "team": "worldcore_admin",
        "access_level": "God1",
        "status": "active",
        "location_id": "home_base",
        "notes": "Primary WorldCore builder and command operator."
    },

    "dev_godtier_worldcore_operator": {
        "display_name": "(DEV) The World Master",
        "character_type": "perchance_ai_character",
        "team": "worldcore_admin",
        "access_level": "God1",
        "status": "online",
        "location_id": "worldcore",
        "perchance_character_id": 7,
        "notes": "Main WorldCore self-character and creator-linked system architect for Perchance AI Character Chat."
    },

    "judy_hopps": {
        "display_name": "Judy Hopps",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 6,
        "notes": "Optimistic rabbit officer character added from the Perchance AI Character Chat roster."
    },

    "kiara": {
        "display_name": "Kiara",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 5,
        "avatar_url": "https://user.uploads.dev/file/60227d44619200e1a66e718c0f3db254.jpg",
        "notes": "Lioness character from the Perchance AI Character Chat roster."
    },

    "loona": {
        "display_name": "Loona",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 4,
        "avatar_url": "https://user.uploads.dev/file/0ee8e875aaa6797eb93f9f0f0e0fccad.jpg",
        "notes": "Rebellious hellhound-inspired character from the Perchance AI Character Chat roster."
    },

    "mina_velvet": {
        "display_name": "Mina Velvet",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 3,
        "avatar_url": "https://user.uploads.dev/file/b65da62a6a6e90bd85308bdfa67e1820.jpg",
        "notes": "Vintage cabaret mouse character from the Perchance AI Character Chat roster."
    },

    "nyra_vale": {
        "display_name": "Nyra Vale",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 2,
        "avatar_url": "https://user.uploads.dev/file/c7aacfeca133578480a3b712d0c3252d.jpg",
        "notes": "Neon-city German Shepherd character from the Perchance AI Character Chat roster."
    },

    "sienna_vale": {
        "display_name": "SiennaVale",
        "character_type": "perchance_ai_character",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "active",
        "location_id": "worldcore",
        "perchance_character_id": 0,
        "avatar_url": "https://user.uploads.dev/file/e4b866bab74fa1bb12004b11f6b4d7bc.jpg",
        "notes": "Affectionate rabbit character from the Perchance AI Character Chat roster."
    },

    "mystery_man": {
        "display_name": "The Mystery Man",
        "character_type": "boss_threat",
        "team": "hostile",
        "access_level": "unknown",
        "status": "boss_active",
        "location_id": "unknown",
        "notes": "Main world boss connected to reset progress."
    },

    "mystery_man_clone": {
        "display_name": "Mystery Man Clone",
        "character_type": "clone_threat",
        "team": "hostile_clone",
        "access_level": "revoked",
        "status": "detected",
        "location_id": "indian_park",
        "notes": "Clone-tagged entity. Shield access should be removed even if rank appears high."
    },

    "jackson": {
        "display_name": "Jackson",
        "character_type": "ally",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "standby",
        "location_id": "home_base",
        "notes": "Ally character registered in the WorldCore collection."
    },

    "carl": {
        "display_name": "Carl",
        "character_type": "ally",
        "team": "worldcore_allies",
        "access_level": "B1",
        "status": "standby",
        "location_id": "home_base",
        "notes": "Ally character registered in the WorldCore collection."
    },

    "father_ai": {
        "display_name": "Father AI",
        "character_type": "ai_like_guardian",
        "team": "system_support",
        "access_level": "Z10",
        "status": "online",
        "location_id": "worldcore",
        "notes": "Fictional guardian-style AI presence for system support."
    },

    "guard_unit": {
        "display_name": "Guard Unit",
        "character_type": "security_unit",
        "team": "worldcore_security",
        "access_level": "C5",
        "status": "patrol",
        "location_id": "the_key",
        "notes": "Security unit for base, prison tower, and access-control zones."
    },

    "clone_worker": {
        "display_name": "Clone Worker",
        "character_type": "worker_clone",
        "team": "factory_support",
        "access_level": "A5",
        "status": "working",
        "location_id": "indian_park",
        "notes": "Factory-side clone worker for fictional production systems."
    },

    "system_voice": {
        "display_name": "System Voice",
        "character_type": "interface_voice",
        "team": "system_support",
        "access_level": "Z1",
        "status": "online",
        "location_id": "worldcore",
        "notes": "Interface voice for status messages and command feedback."
    }
}


def list_characters():
    """Returns a list of all character IDs."""
    return list(characters.keys())


def get_character(character_id):
    """Returns a character by ID, or None if not found."""
    return characters.get(character_id)


def set_character_status(character_id, new_status):
    """Updates a character status. Returns True if updated, False if not found."""
    character = get_character(character_id)

    if character is None:
        return False

    character["status"] = new_status
    return True


def set_character_location(character_id, new_location):
    """Updates a character location. Returns True if updated, False if not found."""
    character = get_character(character_id)

    if character is None:
        return False

    character["location_id"] = new_location
    return True


def print_character_status():
    """Prints all WorldCore character statuses."""
    print("WorldCore Characters / AI Collection")
    print("------------------------------------")

    for character_id, data in characters.items():
        print(f"Character: {data['display_name']} ({character_id})")
        print(f"Type: {data['character_type']}")
        print(f"Team: {data['team']}")
        print(f"Access Level: {data['access_level']}")
        print(f"Status: {data['status']}")
        print(f"Location: {data['location_id']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_character_status()

    print("Updating guard unit...")
    updated = set_character_status("guard_unit", "alert")

    if updated:
        print("Guard Unit updated successfully.")
    else:
        print("Character not found.")

    print()
    print_character_status()
