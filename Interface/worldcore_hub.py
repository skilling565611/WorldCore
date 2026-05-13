# worldcore_hub.py
# Lightweight command-line dashboard for WorldCore.
# Run from the WorldCore folder with: python Interface/worldcore_hub.py

import os
import sys


# Make package imports work when this file is run directly from Interface/.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


MODULE_PATHS = {
    "world_data": "Core.world_data",
    "zones": "Core.zones",
    "characters": "Core.characters",
    "ownership_systems": "Core.ownership_systems",
    "ai_system": "Core.ai_system",
    "cameras": "Systems.cameras",
    "power_system": "Systems.power_system",
    "base_modes": "Core.base_modes",
    "shields": "Security.shields",
    "threats": "Security.threats",
    "transport": "Systems.transport",
    "events": "Systems.events",
    "save_system": "Systems.save_system",
    "world_time": "Core.world_time",
    "access_levels": "Security.access_levels",
    "world_setting": "Core.world_setting",
    "config": "Core.config",
    "registry": "Core.registry",
    "startup": "Core.startup",
    "test_all": "Tests.test_all"
}


def safe_import(import_path):
    """
    Safely imports a module by package path.
    Returns None if the module is missing or has an error.
    """
    try:
        return __import__(import_path, fromlist=["*"])
    except Exception:
        return None


# Load WorldCore modules safely.
modules = {}

for name, import_path in MODULE_PATHS.items():
    modules[name] = safe_import(import_path)


def get_module(module_name):
    """Returns a loaded module, or None if it is missing."""
    return modules.get(module_name)


def run_module_function(module_name, function_name):
    """Runs a module function safely if the module and function exist."""
    module = get_module(module_name)

    if module is None or not hasattr(module, function_name):
        print("Module not available yet.")
        return

    try:
        getattr(module, function_name)()
    except Exception as error:
        print(f"Module error: {error}")


def print_boot_banner():
    """Prints the WorldCore boot banner."""
    print("===================================")
    print("   WorldCore Control Hub Online    ")
    print("===================================")


def print_dashboard_summary():
    """Prints a lightweight summary of the current WorldCore state."""
    print("Dashboard Summary")
    print("-----------------")

    world_setting = get_module("world_setting")
    if world_setting and hasattr(world_setting, "world_setting"):
        setting = world_setting.world_setting
        print(f"Project Name: {setting.get('project_name', 'WorldCore')}")
        print(f"World Setting: {setting.get('setting_type', 'unknown')}")
        print(f"World Status: {setting.get('world_status', 'unknown')}")
    else:
        print("Project Name: WorldCore")
        print("World Setting: Module not available yet.")

    zones = get_module("zones")
    if zones and hasattr(zones, "zones"):
        print(f"Zones: {len(zones.zones)}")
    else:
        print("Zones: Module not available yet.")

    cameras = get_module("cameras")
    if cameras and hasattr(cameras, "fake_cameras"):
        print(f"Fake Cameras: {len(cameras.fake_cameras)}")
    else:
        print("Fake Cameras: Module not available yet.")

    characters = get_module("characters")
    if characters and hasattr(characters, "characters"):
        print(f"Characters / AI Collection: {len(characters.characters)}")
    else:
        print("Characters / AI Collection: Module not available yet.")

    ownership_systems = get_module("ownership_systems")
    if ownership_systems and hasattr(ownership_systems, "ownership_systems"):
        print(f"Ownership & Servitude Systems: {len(ownership_systems.ownership_systems)}")
    else:
        print("Ownership & Servitude Systems: Module not available yet.")

    ai_system = get_module("ai_system")
    if ai_system and hasattr(ai_system, "ai_system"):
        print(f"AI Layer: {ai_system.ai_system.get('status', 'unknown')}")
    else:
        print("AI Layer: Module not available yet.")

    threats = get_module("threats")
    if threats and hasattr(threats, "threats"):
        print(f"Threats: {len(threats.threats)}")
    else:
        print("Threats: Module not available yet.")

    shields = get_module("shields")
    if shields and hasattr(shields, "shields"):
        print(f"Shields: {len(shields.shields)}")
    else:
        print("Shields: Module not available yet.")

    events = get_module("events")
    if events and hasattr(events, "event_log"):
        print(f"Events: {len(events.event_log)}")
    else:
        print("Events: Module not available yet.")


def show_menu():
    """Prints the main WorldCore hub menu."""
    print()
    print("===================================")
    print("        WorldCore Dashboard         ")
    print("===================================")
    print("1. Dashboard Summary")
    print("2. World Status")
    print("3. Zones")
    print("4. Fake Cameras")
    print("5. Characters / AI Collection")
    print("6. Ownership & Servitude Systems")
    print("7. AI Layer / Image Categories")
    print("8. Power System")
    print("9. Base Modes")
    print("10. Shields")
    print("11. Threats")
    print("12. Transport")
    print("13. Events")
    print("14. Save/Load Status")
    print("15. Test All Modules")
    print("0. Exit")
    print("===================================")


def run_test_all():
    """Runs test_all.main() if test_all.py is available."""
    test_all = get_module("test_all")

    if test_all is None or not hasattr(test_all, "main"):
        print("Module not available yet.")
        return

    try:
        test_all.main()
    except Exception as error:
        print(f"Module error: {error}")


def show_ownership_menu():
    """Prints the ownership systems submenu."""
    print()
    print("Ownership & Servitude Systems")
    print("-----------------------------")
    print("1. List ownership systems")
    print("2. View ownership summary")
    print("3. List regional laws")
    print("4. View regional summary")
    print("0. Back")


def run_ownership_option(choice):
    """Runs the selected ownership submenu option."""
    ownership = get_module("ownership_systems")

    if ownership is None:
        print("Module not available yet.")
        return True

    print()

    if choice == "1":
        if hasattr(ownership, "list_ownership_systems"):
            print("Ownership Systems:")
            for system_id in ownership.list_ownership_systems():
                print(f"- {system_id}")
        else:
            print("Module not available yet.")
    elif choice == "2":
        run_module_function("ownership_systems", "print_ownership_summary")
    elif choice == "3":
        if hasattr(ownership, "list_regions"):
            print("Regional Laws:")
            for region_id in ownership.list_regions():
                print(f"- {region_id}")
        else:
            print("Module not available yet.")
    elif choice == "4":
        run_module_function("ownership_systems", "print_region_summary")
    elif choice == "0":
        return False
    else:
        print("Invalid option. Please choose a number from the menu.")

    return True


def run_ownership_menu():
    """Runs the ownership systems submenu."""
    running = True

    while running:
        show_ownership_menu()
        choice = input("Choose an option: ").strip()
        running = run_ownership_option(choice)


def run_option(choice):
    """Runs the selected menu option."""
    print()

    if choice == "1":
        print_dashboard_summary()
    elif choice == "2":
        run_module_function("world_data", "print_world_status")
    elif choice == "3":
        run_module_function("zones", "print_zone_status")
    elif choice == "4":
        run_module_function("cameras", "print_camera_status")
    elif choice == "5":
        run_module_function("characters", "print_character_status")
    elif choice == "6":
        run_ownership_menu()
    elif choice == "7":
        run_module_function("ai_system", "print_ai_status")
    elif choice == "8":
        run_module_function("power_system", "print_power_status")
    elif choice == "9":
        run_module_function("base_modes", "print_base_modes")
    elif choice == "10":
        run_module_function("shields", "print_shield_status")
    elif choice == "11":
        run_module_function("threats", "print_threat_status")
    elif choice == "12":
        run_module_function("transport", "print_transport_status")
    elif choice == "13":
        run_module_function("events", "print_event_log")
    elif choice == "14":
        run_module_function("save_system", "print_save_status")
    elif choice == "15":
        run_test_all()
    elif choice == "0":
        print("Closing WorldCore Control Hub.")
        return False
    else:
        print("Invalid option. Please choose a number from the menu.")

    return True


def main():
    """Runs the WorldCore Control Hub dashboard."""
    print_boot_banner()
    running = True

    while running:
        show_menu()
        choice = input("Choose an option: ").strip()
        running = run_option(choice)


if __name__ == "__main__":
    main()
