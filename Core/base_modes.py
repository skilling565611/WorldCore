# base_modes.py
# Lightweight WorldCore base mode system.
# Bases can switch between different futuristic functions and operating modes.

base_modes = {
    "home_base": {
        "display_name": "Home Base",
        "current_mode": "command_power_mode",
        "available_modes": [
            "command_mode",
            "power_station_mode",
            "recovery_mode",
            "standby_mode"
        ],
        "mode_notes": "Home Base acts as a command point and local power station."
    },

    "the_key": {
        "display_name": "The Key",
        "current_mode": "base_mode",
        "available_modes": [
            "base_mode",
            "prison_tower_mode",
            "control_center_mode",
            "elevator_mode",
            "teleporter_mode",
            "lockdown_mode"
        ],
        "mode_notes": "The Key can switch into prison tower mode and act as a control center, elevator, or teleporter."
    },

    "indian_park": {
        "display_name": "Indian Park / Madison Park",
        "current_mode": "factory_power_mode",
        "available_modes": [
            "factory_mode",
            "power_station_mode",
            "clone_facility_mode",
            "plant_mode",
            "field_operation_mode",
            "standby_mode"
        ],
        "mode_notes": "Indian Park functions as a factory base, power station, clone facility, and plant zone."
    },

    "magic_station": {
        "display_name": "Magic Station",
        "current_mode": "damaged_sensor_mode",
        "available_modes": [
            "sensor_mode",
            "control_center_mode",
            "repair_mode",
            "offline_mode",
            "standby_mode"
        ],
        "mode_notes": "Magic Station is an important control sensor, but it is currently damaged."
    },

    "reservoir_beach": {
        "display_name": "Reservoir Beach",
        "current_mode": "unknown_mode",
        "available_modes": [
            "water_base_mode",
            "cooling_station_mode",
            "resource_node_mode",
            "scan_mode",
            "standby_mode"
        ],
        "mode_notes": "Reservoir Beach acts as a water-side base, cooling station, and resource node."
    }
}


def list_base_modes():
    """Returns all location IDs that have base mode data."""
    return list(base_modes.keys())


def get_base_mode(location_id):
    """Returns base mode data for a location, or None if not found."""
    return base_modes.get(location_id)


def set_base_mode(location_id, new_mode):
    """
    Sets the current mode for a location.
    Returns True if successful.
    Returns False if the location does not exist or the mode is not available.
    """
    base = get_base_mode(location_id)

    if base is None:
        return False

    if new_mode not in base["available_modes"]:
        return False

    base["current_mode"] = new_mode
    return True


def print_base_modes():
    """Prints all base mode statuses."""
    print("WorldCore Base Modes")
    print("--------------------")

    for location_id, data in base_modes.items():
        print(f"Base: {data['display_name']} ({location_id})")
        print(f"Current Mode: {data['current_mode']}")
        print(f"Available Modes: {', '.join(data['available_modes'])}")
        print(f"Notes: {data['mode_notes']}")
        print()


if __name__ == "__main__":
    print_base_modes()

    print("Switching The Key to prison tower mode...")
    updated = set_base_mode("the_key", "prison_tower_mode")

    if updated:
        print("The Key mode updated successfully.")
    else:
        print("Could not update The Key mode.")

    print()
    print_base_modes()
