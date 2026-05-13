# world_data.py
# Lightweight CyberPulse / Inner World data structure.
# This file stores important world locations, threats, systems, and basic helper functions.
# It is intentionally simple so it does not overload VS Code, Codex, or a weaker laptop.


# Main world dictionary.
# This is the central storage area for the CyberPulse inner-world data.
world = {
    "name": "CyberPulse Inner World",

    # Current world status.
    "status": "active",

    # The world reset condition.
    "reset_trigger": "Defeat current Mystery Man Boss",

    # Important world locations and base areas.
    "locations": {
        "home_base": {
            "display_name": "Home Base",
            "type": ["main_base", "power_station"],
            "status": "active",
            "notes": "Main base near home. Can act as a main base and power station, but not really a factory.",
        },

        "the_key": {
            "display_name": "The Key",
            "type": ["base", "prison_tower", "control_center", "teleporter", "elevator"],
            "status": "active",
            "notes": "First base anchor. Can switch into prison tower mode. Includes control center, elevator, and teleporter functions.",
        },

        "indian_park": {
            "display_name": "Indian Park / Madison Park",
            "type": ["factory_base", "power_station", "clone_facility", "plant"],
            "status": "powered",
            "notes": "Factory/base zone with power systems, plant systems, and clone facility functions.",
        },

        "magic_station": {
            "display_name": "Magic Station",
            "type": ["main_control_sensor", "damaged_control_center"],
            "status": "damaged",
            "notes": "Important control sensor near the school area. Currently in poor condition.",
        },

        "reservoir_beach": {
            "display_name": "Reservoir Beach",
            "type": ["water_base", "cooling_station", "resource_node"],
            "status": "unknown",
            "notes": "Reservoir/public beach node. Some people call it the reservoir and some call it the beach.",
        },
    },

    # Main enemies and threats.
    "threats": {
        "mystery_man": {
            "display_name": "The Mystery Man",
            "status": "boss_active",
            "origin": "unknown / corrupted creation",
            "notes": "Current world boss. Must be defeated before the next reset phase.",
        },

        "mystery_man_clones": {
            "display_name": "Mystery Man Clones",
            "status": "contained_some",
            "notes": "Clones can infiltrate systems and must be scanned, tagged, and contained.",
        },
    },

    # Major world systems.
    "systems": {
        "black_hole_shield": {
            "display_name": "Black Hole Shield",
            "level": "highest_single_shield",
            "function": "Pushes out unknown, unauthorized, or flagged entities.",
        },

        "god_level_shield": {
            "display_name": "God-Level Shield",
            "level": "combined_all_shields",
            "function": "All major shields combined into one God-level protection layer.",
        },

        "fast_lane": {
            "display_name": "Fast Lane",
            "type": "underground_transport",
            "vehicle_type": "hovercraft",
            "function": "Fast travel system under the world.",
        },
    },
}


def print_world_status():
    """
    Prints a simple overview of the current world status.
    This is useful for quick testing.
    """
    print(f"World: {world['name']}")
    print(f"Status: {world['status']}")
    print(f"Reset Trigger: {world['reset_trigger']}")
    print()

    print("Locations:")
    for location_id, data in world["locations"].items():
        display_name = data["display_name"]
        status = data["status"]
        location_types = ", ".join(data["type"])
        print(f"- {display_name} ({location_id})")
        print(f"  Status: {status}")
        print(f"  Type: {location_types}")
        print()


def get_location(location_id):
    """
    Returns a location dictionary by its ID.
    If the location does not exist, returns None.
    """
    return world["locations"].get(location_id)


def set_location_status(location_id, new_status):
    """
    Updates the status of a location.
    Returns True if the location exists and was updated.
    Returns False if the location does not exist.
    """
    location = get_location(location_id)

    if location is None:
        return False

    location["status"] = new_status
    return True


def list_locations():
    """
    Returns a list of all location IDs.
    """
    return list(world["locations"].keys())


# Simple test area.
# This only runs when this file is opened directly.
if __name__ == "__main__":
    print_world_status()

    print("Location IDs:")
    print(list_locations())
    print()

    print("Updating The Key status...")
    updated = set_location_status("the_key", "prison_mode_active")

    if updated:
        print("The Key status updated successfully.")
    else:
        print("The Key was not found.")

    print()
    print_world_status()
