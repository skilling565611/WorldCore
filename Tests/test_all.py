# test_all.py
# Lightweight WorldCore module test runner.
# Safely imports known modules and runs their print functions when available.

import os
import sys


# Make package imports work when this file is run directly from Tests/.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


module_paths = {
    "world_data": "Core.world_data",
    "cameras": "Systems.cameras",
    "zones": "Core.zones",
    "characters": "Core.characters",
    "ownership_systems": "Core.ownership_systems",
    "ai_system": "Core.ai_system",
    "world_time": "Core.world_time",
    "access_levels": "Security.access_levels",
    "shields": "Security.shields",
    "world_setting": "Core.world_setting",
    "events": "Systems.events",
    "base_modes": "Core.base_modes",
    "power_system": "Systems.power_system",
    "transport": "Systems.transport",
    "threats": "Security.threats",
    "save_system": "Systems.save_system",
    "config": "Core.config",
    "registry": "Core.registry",
    "startup": "Core.startup"
}

print_functions = {
    "world_data": "print_world_status",
    "cameras": "print_camera_status",
    "zones": "print_zone_status",
    "characters": "print_character_status",
    "ownership_systems": "print_ownership_summary",
    "ai_system": "print_ai_status",
    "world_time": "print_world_time_status",
    "access_levels": "print_access_examples",
    "shields": "print_shield_status",
    "world_setting": "print_world_setting",
    "events": "print_event_log",
    "base_modes": "print_base_modes",
    "power_system": "print_power_status",
    "transport": "print_transport_status",
    "threats": "print_threat_status",
    "save_system": "print_save_status",
    "config": "print_config",
    "registry": "print_registry",
    "startup": "print_startup_status"
}


def safe_import(import_path):
    """Safely imports a module by package path. Returns None if it cannot be loaded."""
    try:
        return __import__(import_path, fromlist=["*"])
    except Exception as error:
        print(f"[Missing or Error] {import_path}: {error}")
        return None


def run_print_function(module_name, module):
    """Runs a module print function if that function exists."""
    function_name = print_functions.get(module_name)

    if function_name is None:
        print(f"No print function registered for {module_name}.")
        return

    if not hasattr(module, function_name):
        print(f"{module_name}.{function_name}() was not found.")
        return

    print()
    print(f"Running {module_name}.{function_name}()")
    print("=" * 40)
    getattr(module, function_name)()


def main():
    """Imports and tests all known WorldCore modules."""
    loaded_modules = {}

    print("WorldCore Module Load Test")
    print("--------------------------")

    for module_name, import_path in module_paths.items():
        module = safe_import(import_path)

        if module is None:
            print(f"{module_name}: missing or failed")
        else:
            loaded_modules[module_name] = module
            print(f"{module_name}: loaded")

    print()
    print("WorldCore Module Print Tests")
    print("----------------------------")

    for module_name, module in loaded_modules.items():
        run_print_function(module_name, module)


if __name__ == "__main__":
    main()
