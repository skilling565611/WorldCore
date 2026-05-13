# world_time.py
# Lightweight WorldCore time system.
# WorldCore time is connected to real-life time, but it runs slightly faster.

from datetime import datetime


world_time_settings = {
    "time_mode": "near_real_time",
    "speed_multiplier": 1.15,
    "description": "WorldCore time runs slightly faster than real life, but stays close to real-world timing.",
    "last_checked": None
}


def get_world_time_settings():
    """Returns the WorldCore time settings."""
    return world_time_settings


def set_speed_multiplier(new_multiplier):
    """Updates the WorldCore time speed multiplier."""
    if new_multiplier <= 0:
        return False

    world_time_settings["speed_multiplier"] = new_multiplier
    return True


def calculate_world_minutes(real_minutes):
    """Converts real-life minutes into WorldCore minutes."""
    return real_minutes * world_time_settings["speed_multiplier"]


def print_world_time_status():
    """Prints the current WorldCore time settings."""
    world_time_settings["last_checked"] = datetime.now().isoformat(timespec="seconds")

    print("WorldCore Time Status")
    print("---------------------")
    print(f"Mode: {world_time_settings['time_mode']}")
    print(f"Speed Multiplier: {world_time_settings['speed_multiplier']}")
    print(f"Description: {world_time_settings['description']}")
    print(f"Last Checked: {world_time_settings['last_checked']}")
    print()


if __name__ == "__main__":
    print_world_time_status()

    real_minutes = 60
    world_minutes = calculate_world_minutes(real_minutes)

    print(f"{real_minutes} real minutes = {world_minutes:.2f} WorldCore minutes")
