# zones.py
# Lightweight WorldCore zone system.
# These zones are real-life anchor places connected to the inner-world/game layer.
# This file does NOT use GPS, maps, internet, tracking, or real location services.

zones = {
    "home_zone": {
        "display_name": "Home Zone",
        "real_life_type": "home_area",
        "world_role": ["main_base", "power_station", "command_point"],
        "status": "active",
        "notes": "Main personal base area. Used for command, recovery, and power support."
    },

    "the_key_zone": {
        "display_name": "The Key Zone",
        "real_life_type": "old_corner_lot",
        "world_role": ["first_base", "prison_tower", "elevator", "teleporter", "control_center"],
        "status": "active",
        "notes": "Old base anchor with the key-like sign. Can switch into prison tower mode."
    },

    "indian_park_zone": {
        "display_name": "Indian Park / Madison Park Zone",
        "real_life_type": "park",
        "world_role": ["factory_base", "power_station", "clone_facility", "plant_zone"],
        "status": "powered",
        "notes": "Factory base and power area. Used for production, clone systems, and field operations."
    },

    "magic_station_zone": {
        "display_name": "Magic Station Zone",
        "real_life_type": "park_school_area",
        "world_role": ["main_control_sensor", "damaged_control_center"],
        "status": "damaged",
        "notes": "Control sensor near the school area. Important but in poor condition."
    },

    "reservoir_beach_zone": {
        "display_name": "Reservoir / Public Beach Zone",
        "real_life_type": "reservoir_beach",
        "world_role": ["water_base", "cooling_station", "resource_node"],
        "status": "unknown",
        "notes": "Reservoir area used as a public beach. Water-side base and cooling/resource node."
    }
}


def list_zones():
    """Returns a list of all zone IDs."""
    return list(zones.keys())


def get_zone(zone_id):
    """Returns a zone by ID, or None if it does not exist."""
    return zones.get(zone_id)


def set_zone_status(zone_id, new_status):
    """Updates a zone status. Returns True if updated, False if zone was not found."""
    zone = get_zone(zone_id)

    if zone is None:
        return False

    zone["status"] = new_status
    return True


def print_zone_status():
    """Prints all WorldCore zone statuses."""
    print("WorldCore Zone Status")
    print("---------------------")

    for zone_id, data in zones.items():
        print(f"Zone: {data['display_name']} ({zone_id})")
        print(f"Real-Life Type: {data['real_life_type']}")
        print(f"World Role: {', '.join(data['world_role'])}")
        print(f"Status: {data['status']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_zone_status()

    print("Zone IDs:")
    print(list_zones())
    print()

    print("Updating The Key Zone...")
    updated = set_zone_status("the_key_zone", "prison_tower_mode")

    if updated:
        print("The Key Zone updated successfully.")
    else:
        print("Zone not found.")

    print()
    print_zone_status()
