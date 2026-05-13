# project_health.py
# Lightweight WorldCore project health checker.
# Reads/checks important folders and files, then prints a clear report.

import os


REQUIRED_FOLDERS = [
    "Core",
    "Systems",
    "Security",
    "Interface",
    "Data",
    "Tests",
    "Docs",
    "Tools"
]

REQUIRED_FILES = {
    "Core": [
        "world_data.py",
        "world_setting.py",
        "world_time.py",
        "zones.py",
        "base_modes.py",
        "config.py",
        "registry.py",
        "startup.py"
    ],
    "Systems": [
        "cameras.py",
        "power_system.py",
        "transport.py",
        "events.py",
        "save_system.py"
    ],
    "Security": [
        "access_levels.py",
        "shields.py",
        "threats.py"
    ],
    "Interface": [
        "worldcore_hub.py"
    ],
    "Tests": [
        "test_all.py"
    ],
    "Docs": [
        "README.md"
    ],
    "Tools": [
        "backup_manager.py",
        "project_health.py"
    ]
}


def get_project_root():
    """Returns the active WorldCore project folder."""
    tools_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_folder)


def check_folder(path):
    """Returns True if a folder exists, otherwise False."""
    try:
        return os.path.isdir(path)
    except Exception:
        return False


def check_file(path):
    """Returns True if a file exists, otherwise False."""
    try:
        return os.path.isfile(path)
    except Exception:
        return False


def get_health_status(missing_count):
    """Returns a simple project health label."""
    if missing_count == 0:
        return "PERFECT"

    if missing_count <= 3:
        return "OK"

    return "NEEDS WORK"


def run_health_check():
    """Runs the WorldCore folder/file health check."""
    project_root = get_project_root()
    total_checked = 0
    found_count = 0
    missing_count = 0

    print("WorldCore Project Health Check")
    print("------------------------------")
    print(f"Project Root: {project_root}")
    print()

    print("Folders")
    print("-------")

    for folder_name in REQUIRED_FOLDERS:
        folder_path = os.path.join(project_root, folder_name)
        total_checked += 1

        if check_folder(folder_path):
            found_count += 1
            print(f"FOUND   {folder_name}")
        else:
            missing_count += 1
            print(f"MISSING {folder_name}")

    print()
    print("Files")
    print("-----")

    for folder_name, file_names in REQUIRED_FILES.items():
        for file_name in file_names:
            file_path = os.path.join(project_root, folder_name, file_name)
            label = os.path.join(folder_name, file_name)
            total_checked += 1

            if check_file(file_path):
                found_count += 1
                print(f"FOUND   {label}")
            else:
                missing_count += 1
                print(f"MISSING {label}")

    print()
    print("Summary")
    print("-------")
    print(f"Total Checked: {total_checked}")
    print(f"Found: {found_count}")
    print(f"Missing: {missing_count}")
    print(f"Health Status: {get_health_status(missing_count)}")


if __name__ == "__main__":
    run_health_check()
