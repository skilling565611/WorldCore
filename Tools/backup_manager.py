# backup_manager.py
# Lightweight WorldCore backup manager.
# Creates milestone backups beside the active WorldCore folder.

import os
import shutil
from datetime import datetime


BACKUP_FOUNDATION = "WorldCore_Backup_01_Foundation_Working"
BACKUP_HUB_UPGRADE = "WorldCore_Backup_02_Hub_Upgrade_Working"
BACKUP_INTERFACE_START = "WorldCore_Backup_03_Interface_Start"


def get_worldcore_folder():
    """Returns the active WorldCore folder path."""
    tools_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_folder)


def get_backup_parent_folder():
    """Returns the folder where WorldCore milestone backups should be created."""
    worldcore_folder = get_worldcore_folder()
    return os.path.dirname(worldcore_folder)


def create_backup(backup_name):
    """
    Creates a milestone backup beside the WorldCore folder.
    Does not overwrite an existing backup folder.

    TODO: Add an ignore list before using this for routine backups so .git,
    .venv, caches, logs, and generated files are not copied unintentionally.
    """
    source_folder = get_worldcore_folder()
    backup_parent = get_backup_parent_folder()
    backup_path = os.path.join(backup_parent, backup_name)

    if os.path.exists(backup_path):
        print(f"Backup already exists: {backup_path}")
        return False

    try:
        print(f"Creating backup: {backup_name}")
        print(f"Source: {source_folder}")
        print(f"Target: {backup_path}")
        shutil.copytree(source_folder, backup_path)
        print(f"Backup created successfully at {datetime.now().isoformat(timespec='seconds')}")
        return True
    except Exception as error:
        print(f"Backup failed: {error}")
        return False


def backup_foundation():
    """Creates the foundation working backup."""
    return create_backup(BACKUP_FOUNDATION)


def backup_hub_upgrade():
    """Creates the hub upgrade working backup."""
    return create_backup(BACKUP_HUB_UPGRADE)


def backup_interface_start():
    """Creates the interface start backup."""
    return create_backup(BACKUP_INTERFACE_START)


def list_backups():
    """Lists known milestone backup folders and whether they exist."""
    backup_parent = get_backup_parent_folder()
    backup_names = [
        BACKUP_FOUNDATION,
        BACKUP_HUB_UPGRADE,
        BACKUP_INTERFACE_START
    ]

    print("WorldCore Backup Milestones")
    print("---------------------------")

    for backup_name in backup_names:
        backup_path = os.path.join(backup_parent, backup_name)

        if os.path.exists(backup_path):
            print(f"{backup_name}: exists")
        else:
            print(f"{backup_name}: not created")


def show_menu():
    """Prints the backup manager menu."""
    print()
    print("WorldCore Backup Manager")
    print("------------------------")
    print("1. Create Foundation Backup")
    print("2. Create Hub Upgrade Backup")
    print("3. Create Interface Start Backup")
    print("4. List Backups")
    print("0. Exit")


def run_option(choice):
    """Runs the selected backup manager option."""
    print()

    if choice == "1":
        backup_foundation()
    elif choice == "2":
        backup_hub_upgrade()
    elif choice == "3":
        backup_interface_start()
    elif choice == "4":
        list_backups()
    elif choice == "0":
        print("Closing backup manager.")
        return False
    else:
        print("Invalid option. Please choose a number from the menu.")

    return True


def main():
    """Runs the backup manager command-line menu."""
    running = True

    while running:
        show_menu()
        choice = input("Choose an option: ").strip()
        running = run_option(choice)


if __name__ == "__main__":
    main()
