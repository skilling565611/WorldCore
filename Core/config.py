# config.py
# Lightweight WorldCore configuration values.

config = {
    "project_name": "WorldCore",
    "version": "0.1",
    "mode": "lightweight_cli",
    "data_folder": "Data",
    "save_file": "world_state.json",
    "backup_file": "world_state_backup.json"
}


def get_config():
    """Returns the WorldCore config dictionary."""
    return config


def print_config():
    """Prints the current WorldCore config."""
    print("WorldCore Config")
    print("----------------")
    for key, value in config.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_config()
