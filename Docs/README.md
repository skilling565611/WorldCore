# WorldCore

WorldCore is a lightweight futuristic inner-world control system.

It is not the full world engine yet. It is the foundation layer for organizing locations, zones, fake cameras, characters, ownership and servitude systems, access levels, shields, base modes, events, transport, power, save/load, and world time.

## Folder Structure

```text
WorldCore/
|-- Core/
|   |-- __init__.py
|   |-- world_data.py
|   |-- world_setting.py
|   |-- world_time.py
|   |-- zones.py
|   |-- base_modes.py
|   |-- characters.py
|   |-- ownership_systems.py
|   |-- config.py
|   |-- registry.py
|   `-- startup.py
|-- Systems/
|   |-- __init__.py
|   |-- cameras.py
|   |-- power_system.py
|   |-- transport.py
|   |-- events.py
|   `-- save_system.py
|-- Security/
|   |-- __init__.py
|   |-- access_levels.py
|   |-- shields.py
|   `-- threats.py
|-- Interface/
|   |-- __init__.py
|   `-- worldcore_hub.py
|-- Data/
|-- Tests/
|   |-- __init__.py
|   `-- test_all.py
|-- Tools/
|   |-- backup_manager.py
|   |-- project_health.py
|   `-- perchance_file_scanner.py
`-- Docs/
    `-- README.md
```

## How to Run

Open a terminal inside the WorldCore folder and run:

```bash
python Interface/worldcore_hub.py
```

## Current Goal

Keep WorldCore lightweight and easy to test.

The full world is huge, but this project starts as a simple control dashboard foundation.
