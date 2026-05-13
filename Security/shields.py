# shields.py
# Lightweight WorldCore shield system.
# Shields protect locations, control access, and help block Mystery Man clone activity.

shields = {
    "basic_shield": {
        "display_name": "Basic Shield",
        "shield_type": "standard",
        "power_level": 1,
        "status": "online",
        "function": "Basic protection and simple access filtering.",
        "notes": "Low-level shield used for normal areas."
    },

    "main_shield": {
        "display_name": "Main Shield",
        "shield_type": "base_defense",
        "power_level": 5,
        "status": "online",
        "function": "Protects bases and supports rank-class access control.",
        "notes": "Main defensive shield for important WorldCore facilities."
    },

    "black_hole_shield": {
        "display_name": "Black Hole Shield",
        "shield_type": "highest_single_shield",
        "power_level": 10,
        "status": "online",
        "function": "Pushes out unknown, unauthorized, or Mystery Man-tagged entities.",
        "notes": "Usually the highest single shield level."
    },

    "god_level_shield": {
        "display_name": "God-Level Shield",
        "shield_type": "combined_all_shields",
        "power_level": 999,
        "status": "standby",
        "function": "All shields combined into one God-level protection layer.",
        "notes": "Activates when all major shields combine."
    }
}


def list_shields():
    """Returns a list of all shield IDs."""
    return list(shields.keys())


def get_shield(shield_id):
    """Returns a shield by ID, or None if it does not exist."""
    return shields.get(shield_id)


def set_shield_status(shield_id, new_status):
    """Updates a shield status. Returns True if updated, False if shield was not found."""
    shield = get_shield(shield_id)

    if shield is None:
        return False

    shield["status"] = new_status
    return True


def combine_all_shields():
    """
    Activates God-Level Shield mode.
    This represents all major shields combining together.
    """
    for shield in shields.values():
        shield["status"] = "combined"

    shields["god_level_shield"]["status"] = "active"
    return True


def is_entity_blocked(entity_tag):
    """
    Checks if an entity should be blocked by the shield system.
    Mystery Man clone tags always trigger access removal.
    """
    blocked_tags = [
        "mystery_man_clone",
        "mystery_man_tagged",
        "unknown_hostile"
    ]

    return entity_tag in blocked_tags


def print_shield_status():
    """Prints all WorldCore shield statuses."""
    print("WorldCore Shield Status")
    print("-----------------------")

    for shield_id, data in shields.items():
        print(f"Shield: {data['display_name']} ({shield_id})")
        print(f"Type: {data['shield_type']}")
        print(f"Power Level: {data['power_level']}")
        print(f"Status: {data['status']}")
        print(f"Function: {data['function']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_shield_status()

    print("Testing blocked entity:")
    print("mystery_man_clone blocked:", is_entity_blocked("mystery_man_clone"))
    print()

    print("Combining all shields...")
    combine_all_shields()
    print()

    print_shield_status()
