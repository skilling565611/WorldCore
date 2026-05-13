# power_system.py
# Lightweight WorldCore power system.
# Tracks fictional power nodes for important WorldCore bases.

power_nodes = {
    "home_base": {
        "display_name": "Home Base Power Node",
        "power_level": 90,
        "status": "online",
        "power_source": "local_command_core",
        "notes": "Main local power support for command and recovery systems."
    },

    "the_key": {
        "display_name": "The Key Power Node",
        "power_level": 80,
        "status": "online",
        "power_source": "base_anchor_core",
        "notes": "Supports control center, elevator, teleporter, and prison tower modes."
    },

    "indian_park": {
        "display_name": "Indian Park Factory Power Node",
        "power_level": 95,
        "status": "online",
        "power_source": "factory_power_grid",
        "notes": "High-output power node for factory, clone facility, and plant systems."
    },

    "magic_station": {
        "display_name": "Magic Station Sensor Power Node",
        "power_level": 35,
        "status": "damaged",
        "power_source": "damaged_sensor_core",
        "notes": "Weak power output. Repair is needed before full control functions return."
    },

    "reservoir_beach": {
        "display_name": "Reservoir Beach Water Power Node",
        "power_level": 50,
        "status": "online",
        "power_source": "water_side_resource_node",
        "notes": "Water-side node for cooling, scanning, and resource support."
    }
}


def list_power_nodes():
    """Returns a list of all power node IDs."""
    return list(power_nodes.keys())


def get_power_node(node_id):
    """Returns a power node by ID, or None if it does not exist."""
    return power_nodes.get(node_id)


def set_power_status(node_id, status):
    """Updates a power node status. Returns True if updated, False if not found."""
    node = get_power_node(node_id)

    if node is None:
        return False

    node["status"] = status
    return True


def clamp_power_level(level):
    """Keeps power level between 0 and 100."""
    if level < 0:
        return 0

    if level > 100:
        return 100

    return level


def set_power_level(node_id, level):
    """Updates a power node level. Returns True if updated, False if not found."""
    node = get_power_node(node_id)

    if node is None:
        return False

    node["power_level"] = clamp_power_level(level)

    if node["power_level"] == 0:
        node["status"] = "offline"
    elif node["status"] != "damaged":
        node["status"] = "online"

    return True


def power_up_node(node_id):
    """Sets a power node to full power unless it does not exist."""
    return set_power_level(node_id, 100)


def power_down_node(node_id):
    """Sets a power node to zero power and marks it offline."""
    return set_power_level(node_id, 0)


def is_node_online(node_id):
    """Returns True if a power node exists and is online with power above zero."""
    node = get_power_node(node_id)

    if node is None:
        return False

    return node["status"] == "online" and node["power_level"] > 0


def print_power_summary():
    """Prints a short summary of power node counts."""
    total_nodes = len(power_nodes)
    online_nodes = 0
    offline_nodes = 0
    damaged_nodes = 0

    for node in power_nodes.values():
        if node["status"] == "damaged":
            damaged_nodes += 1
        elif node["status"] == "offline":
            offline_nodes += 1
        elif node["power_level"] > 0:
            online_nodes += 1

    print("WorldCore Power Summary")
    print("-----------------------")
    print(f"Total Nodes: {total_nodes}")
    print(f"Online Nodes: {online_nodes}")
    print(f"Offline Nodes: {offline_nodes}")
    print(f"Damaged Nodes: {damaged_nodes}")


def print_power_status():
    """Prints all WorldCore power node statuses."""
    print("WorldCore Power Status")
    print("----------------------")

    for node_id, data in power_nodes.items():
        print(f"Power Node: {data['display_name']} ({node_id})")
        print(f"Power Level: {data['power_level']}")
        print(f"Status: {data['status']}")
        print(f"Power Source: {data['power_source']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_power_status()

    print("Updating Magic Station power...")
    updated = set_power_status("magic_station", "repair_pending")

    if updated:
        print("Magic Station power status updated successfully.")
    else:
        print("Power node not found.")

    print()
    print_power_status()
