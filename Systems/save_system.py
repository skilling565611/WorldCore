# save_system.py
# Lightweight WorldCore save/load system.
# Saves simple dictionary data to local JSON files only.

import json
import os


SAVE_FILE = "world_state.json"
BACKUP_FILE = "world_state_backup.json"


def save_state(data):
    """
    Saves WorldCore state data to world_state.json.
    Returns True if saved, False if there was an error.
    """
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False


def load_state():
    """
    Loads WorldCore state data from world_state.json.
    Returns an empty dictionary if no save exists or loading fails.
    """
    if not os.path.exists(SAVE_FILE):
        return {}

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}


def backup_state():
    """
    Copies the current save data into world_state_backup.json.
    Returns True if backup was saved, False if no save exists or backup fails.
    """
    data = load_state()

    if not data:
        return False

    try:
        with open(BACKUP_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False


def print_save_status():
    """Prints the current save/load file status."""
    print("WorldCore Save/Load Status")
    print("--------------------------")
    print(f"Save File: {SAVE_FILE}")
    print(f"Save Exists: {os.path.exists(SAVE_FILE)}")
    print(f"Backup File: {BACKUP_FILE}")
    print(f"Backup Exists: {os.path.exists(BACKUP_FILE)}")


if __name__ == "__main__":
    print_save_status()

    print()
    print("Saving test state...")
    saved = save_state({
        "project_name": "WorldCore",
        "status": "test_save"
    })
    print("Saved:", saved)

    print()
    print("Loaded State:")
    print(load_state())

    print()
    print("Creating backup...")
    print("Backup:", backup_state())

    print()
    print_save_status()
