# world_setting.py
# Lightweight WorldCore setting rules.
# WorldCore is futuristic, but it uses real-life places as anchor zones.

world_setting = {
    "project_name": "WorldCore",
    "setting_type": "futuristic_inner_world",
    "technology_level": "advanced_future",
    "real_life_anchor_mode": True,
    "world_status": "under_construction",
    "tone": ["cinematic", "sci_fi", "system_core", "personal_world"],
    "description": (
        "WorldCore is a future-tech interface layer built on top of real-life anchor zones. "
        "Real-world places act as anchors, while the WorldCore layer transforms them into "
        "bases, power stations, factories, prisons, clone facilities, shields, sensors, "
        "teleporters, elevators, and control systems."
    )
}


def get_world_setting():
    """Returns the WorldCore setting dictionary."""
    return world_setting


def update_world_status(new_status):
    """Updates the current WorldCore world status."""
    world_setting["world_status"] = new_status
    return True


def print_world_setting():
    """Prints the current WorldCore setting rules."""
    print("WorldCore Setting")
    print("-----------------")
    print(f"Project Name: {world_setting['project_name']}")
    print(f"Setting Type: {world_setting['setting_type']}")
    print(f"Technology Level: {world_setting['technology_level']}")
    print(f"Real-Life Anchor Mode: {world_setting['real_life_anchor_mode']}")
    print(f"World Status: {world_setting['world_status']}")
    print(f"Tone: {', '.join(world_setting['tone'])}")
    print(f"Description: {world_setting['description']}")


if __name__ == "__main__":
    print_world_setting()

    print()
    print("Updating world status...")
    update_world_status("active_foundation")

    print()
    print_world_setting()
