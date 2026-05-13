# startup.py
# Lightweight startup helpers for WorldCore.

try:
    from Core import config
    from Core import registry
except Exception:
    config = None
    registry = None


def print_startup_banner():
    """Prints the WorldCore startup banner."""
    print("===================================")
    print("   WorldCore Control Hub Online    ")
    print("===================================")


def print_startup_status():
    """Prints simple startup status information."""
    print("WorldCore Startup Status")
    print("------------------------")

    if config and hasattr(config, "config"):
        print(f"Project: {config.config.get('project_name', 'WorldCore')}")
        print(f"Mode: {config.config.get('mode', 'unknown')}")
    else:
        print("Config: Module not available yet.")

    if registry and hasattr(registry, "module_registry"):
        print(f"Registered Modules: {len(registry.module_registry)}")
    else:
        print("Registry: Module not available yet.")


if __name__ == "__main__":
    print_startup_banner()
    print_startup_status()
