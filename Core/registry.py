# registry.py
# Lightweight registry of WorldCore modules and package paths.

module_registry = {
    "world_data": "Core.world_data",
    "world_setting": "Core.world_setting",
    "world_time": "Core.world_time",
    "zones": "Core.zones",
    "base_modes": "Core.base_modes",
    "characters": "Core.characters",
    "ownership_systems": "Core.ownership_systems",
    "ai_system": "Core.ai_system",
    "config": "Core.config",
    "cameras": "Systems.cameras",
    "power_system": "Systems.power_system",
    "transport": "Systems.transport",
    "events": "Systems.events",
    "save_system": "Systems.save_system",
    "access_levels": "Security.access_levels",
    "shields": "Security.shields",
    "threats": "Security.threats",
    "worldcore_hub": "Interface.worldcore_hub",
    "test_all": "Tests.test_all"
}


def list_registered_modules():
    """Returns all registered module names."""
    return list(module_registry.keys())


def get_module_path(module_name):
    """Returns the import path for a registered module, or None."""
    return module_registry.get(module_name)


def safe_import(module_name):
    """Safely imports a registered module by short name or import path."""
    import_path = module_registry.get(module_name, module_name)

    try:
        return __import__(import_path, fromlist=["*"])
    except Exception:
        return None


def print_registry():
    """Prints the WorldCore module registry."""
    print("WorldCore Module Registry")
    print("-------------------------")
    for module_name, import_path in module_registry.items():
        print(f"{module_name}: {import_path}")


if __name__ == "__main__":
    print_registry()
