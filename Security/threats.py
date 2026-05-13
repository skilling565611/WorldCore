# threats.py
# Lightweight WorldCore threat tracking system.
# Tracks fictional threats, lockouts, and corrupted access states.

threats = {
    "mystery_man_boss": {
        "display_name": "Mystery Man Boss",
        "threat_level": "boss",
        "status": "active",
        "location_id": "unknown",
        "notes": "Main current boss threat. Reset progress depends on defeating this threat."
    },

    "mystery_man_clones": {
        "display_name": "Mystery Man Clones",
        "threat_level": "high",
        "status": "detected",
        "location_id": "indian_park",
        "notes": "Clone activity can infiltrate systems and trigger shield access removal."
    },

    "corrupted_access": {
        "display_name": "Corrupted Access",
        "threat_level": "medium",
        "status": "watch",
        "location_id": "the_key",
        "notes": "Access corruption may affect rank control, base permissions, and elevator systems."
    },

    "system_lockout": {
        "display_name": "System Lockout",
        "threat_level": "medium",
        "status": "standby",
        "location_id": "worldcore",
        "notes": "Lockout state can block control hub actions until cleared."
    }
}


def list_threats():
    """Returns a list of all threat IDs."""
    return list(threats.keys())


def get_threat(threat_id):
    """Returns a threat by ID, or None if it does not exist."""
    return threats.get(threat_id)


def set_threat_status(threat_id, status):
    """Updates a threat status. Returns True if updated, False if not found."""
    threat = get_threat(threat_id)

    if threat is None:
        return False

    threat["status"] = status
    return True


def print_threat_status():
    """Prints all WorldCore threat statuses."""
    print("WorldCore Threat Status")
    print("-----------------------")

    for threat_id, data in threats.items():
        print(f"Threat: {data['display_name']} ({threat_id})")
        print(f"Threat Level: {data['threat_level']}")
        print(f"Status: {data['status']}")
        print(f"Location: {data['location_id']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_threat_status()

    print("Updating Mystery Man clones...")
    updated = set_threat_status("mystery_man_clones", "contained_some")

    if updated:
        print("Mystery Man clone threat updated successfully.")
    else:
        print("Threat not found.")

    print()
    print_threat_status()
