# transport.py
# Lightweight WorldCore transport system.
# Tracks fictional movement systems used inside the WorldCore layer.

transport_systems = {
    "bike_mobile_control": {
        "display_name": "Bike Mobile Control",
        "status": "online",
        "transport_type": "mobile_command_vehicle",
        "linked_locations": ["home_base", "the_key", "indian_park"],
        "notes": "Mobile control system used for local travel and quick command access."
    },

    "fast_lane": {
        "display_name": "Fast Lane",
        "status": "active",
        "transport_type": "underground_transport",
        "linked_locations": ["home_base", "the_key", "indian_park", "magic_station", "reservoir_beach"],
        "notes": "Fast underground route system for moving between major WorldCore anchors."
    },

    "hovercraft_network": {
        "display_name": "Hovercraft Network",
        "status": "standby",
        "transport_type": "hovercraft",
        "linked_locations": ["the_key", "indian_park", "reservoir_beach"],
        "notes": "Hovercraft-based transport system connected to the Fast Lane."
    },

    "teleporter_network": {
        "display_name": "Teleporter Network",
        "status": "limited",
        "transport_type": "teleporter",
        "linked_locations": ["the_key", "home_base"],
        "notes": "Limited teleport system anchored through The Key and control systems."
    }
}


def list_transport_systems():
    """Returns a list of all transport system IDs."""
    return list(transport_systems.keys())


def get_transport(system_id):
    """Returns a transport system by ID, or None if it does not exist."""
    return transport_systems.get(system_id)


def set_transport_status(system_id, status):
    """Updates a transport system status. Returns True if updated, False if not found."""
    transport = get_transport(system_id)

    if transport is None:
        return False

    transport["status"] = status
    return True


def print_transport_status():
    """Prints all WorldCore transport system statuses."""
    print("WorldCore Transport Status")
    print("--------------------------")

    for system_id, data in transport_systems.items():
        print(f"Transport: {data['display_name']} ({system_id})")
        print(f"Status: {data['status']}")
        print(f"Type: {data['transport_type']}")
        print(f"Linked Locations: {', '.join(data['linked_locations'])}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_transport_status()

    print("Activating hovercraft network...")
    updated = set_transport_status("hovercraft_network", "active")

    if updated:
        print("Hovercraft network updated successfully.")
    else:
        print("Transport system not found.")

    print()
    print_transport_status()
