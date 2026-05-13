# perchance_file_scanner.py
# Lightweight metadata scanner for future Perchance AI Character Chat files.
# This tool does not connect to Perchance, use networking, or print full file contents.

import gzip
import json
import os


SCAN_EXTENSIONS = [
    ".json",
    ".js",
    ".txt",
    ".md",
    ".gz"
]

FILENAME_KEYWORDS = [
    "perchance",
    "character",
    "ai",
    "chatbot",
    "bot",
    "command",
    "commands",
    "javascript",
    "script",
    "json",
    "database",
    "backup",
    "export",
    "bundle"
]


def get_project_root():
    """Returns the active WorldCore project folder."""
    tools_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_folder)


def get_ai_folder():
    """Returns the WorldCore AI folder path."""
    return os.path.join(get_project_root(), "AI")


def is_possible_ai_file(file_name):
    """Returns True if a filename looks related to AI character chat data."""
    lower_name = file_name.lower()

    for keyword in FILENAME_KEYWORDS:
        if keyword in lower_name:
            return True

    return False


def get_possible_purpose(file_name):
    """Returns a simple purpose guess based on the filename."""
    lower_name = file_name.lower()

    if "backup" in lower_name:
        return "backup"
    if "export" in lower_name:
        return "export"
    if "database" in lower_name or "json" in lower_name:
        return "database_or_json_data"
    if "command" in lower_name or "commands" in lower_name:
        return "commands"
    if "script" in lower_name or "javascript" in lower_name:
        return "script"
    if "character" in lower_name or "chatbot" in lower_name or "bot" in lower_name:
        return "character_chat_data"
    if "bundle" in lower_name:
        return "compressed_or_grouped_bundle"

    return "possible_perchance_ai_file"


def scan_folder(folder_path, results, scanned_paths):
    """
    Scans one folder for possible Perchance AI Character Chat files.
    Adds safe metadata results to the shared results list.
    """
    try:
        folder_path = os.path.abspath(folder_path)

        if not os.path.isdir(folder_path):
            return

        for current_folder, folder_names, file_names in os.walk(folder_path):
            folder_names[:] = [
                folder_name for folder_name in folder_names
                if folder_name != "__pycache__"
            ]

            for file_name in file_names:
                file_extension = os.path.splitext(file_name)[1].lower()

                if file_extension not in SCAN_EXTENSIONS:
                    continue

                if not is_possible_ai_file(file_name):
                    continue

                file_path = os.path.abspath(os.path.join(current_folder, file_name))

                if file_path in scanned_paths:
                    continue

                scanned_paths.append(file_path)

                result = {
                    "file_path": file_path,
                    "file_type": file_extension,
                    "possible_purpose": get_possible_purpose(file_name),
                    "json_valid": None,
                    "top_level_keys": [],
                    "compressed": file_extension == ".gz",
                    "possible_json": None,
                    "dexie_export": None
                }

                if file_extension == ".json":
                    json_result = scan_json_file(file_path)
                    result["json_valid"] = json_result["json_valid"]
                    result["top_level_keys"] = json_result["top_level_keys"]
                    result["dexie_export"] = json_result["dexie_export"]

                    if json_result["dexie_export"]:
                        result["possible_purpose"] = json_result["dexie_export"]["classification"]

                if file_extension == ".gz":
                    gz_result = scan_gz_file(file_path)
                    result["compressed"] = gz_result["compressed"]
                    result["possible_json"] = gz_result["possible_json"]
                    result["json_valid"] = gz_result["json_valid"]
                    result["top_level_keys"] = gz_result["top_level_keys"]
                    result["dexie_export"] = gz_result["dexie_export"]

                    if gz_result["dexie_export"]:
                        result["possible_purpose"] = gz_result["dexie_export"]["classification"]

                results.append(result)

    except Exception:
        return


def get_top_level_keys(data):
    """Returns safe top-level JSON structure names without printing values."""
    if isinstance(data, dict):
        return list(data.keys())

    if isinstance(data, list):
        return ["list"]

    return [type(data).__name__]


def has_value(data, key):
    """Returns yes/no for whether a safe metadata field is present."""
    if not isinstance(data, dict):
        return "no"

    value = data.get(key)

    if value is None:
        return "no"

    if value == "":
        return "no"

    if value == []:
        return "no"

    if value == {}:
        return "no"

    return "yes"


def safe_count(value):
    """Returns a safe count for lists and dictionaries."""
    if isinstance(value, list):
        return len(value)

    if isinstance(value, dict):
        return len(value)

    if value:
        return 1

    return 0


def get_safe_character_source(row):
    """Returns the likely character object inside a Dexie row."""
    if not isinstance(row, dict):
        return {}

    for key in ["character", "data", "value"]:
        nested = row.get(key)

        if isinstance(nested, dict):
            return nested

    return row


def get_first_available(data, keys):
    """Gets the first safe metadata value from a list of possible keys."""
    if not isinstance(data, dict):
        return None

    for key in keys:
        if key in data:
            return data.get(key)

    return None


def get_scene_metadata(character):
    """Returns safe yes/no scene metadata without printing media URLs."""
    scene = character.get("scene")

    if not isinstance(scene, dict):
        scene = {}

    has_background = "no"
    has_music = "no"

    background_keys = [
        "background",
        "backgroundImage",
        "backgroundUrl",
        "sceneBackground",
        "sceneBackgroundUrl"
    ]
    music_keys = [
        "music",
        "musicUrl",
        "backgroundMusic",
        "sceneMusic",
        "sceneMusicUrl"
    ]

    for key in background_keys:
        if has_value(character, key) == "yes" or has_value(scene, key) == "yes":
            has_background = "yes"

    for key in music_keys:
        if has_value(character, key) == "yes" or has_value(scene, key) == "yes":
            has_music = "yes"

    return {
        "has_scene_background": has_background,
        "has_scene_music": has_music
    }


def get_safe_character_metadata(row):
    """
    Returns safe character metadata only.
    Does not include prompts, custom code, messages, URLs, tokens, or media contents.
    """
    character = get_safe_character_source(row)
    scene_metadata = get_scene_metadata(character)

    return {
        "character_name": get_first_available(
            character,
            ["name", "displayName", "characterName", "title"]
        ),
        "modelName": character.get("modelName"),
        "fitMessagesInContextMethod": character.get("fitMessagesInContextMethod"),
        "autoGenerateMemories": character.get("autoGenerateMemories"),
        "has_roleInstruction": has_value(character, "roleInstruction"),
        "has_reminderMessage": has_value(character, "reminderMessage"),
        "has_generalWritingInstructions": has_value(character, "generalWritingInstructions"),
        "has_customCode": has_value(character, "customCode"),
        "shortcutButtons_count": safe_count(character.get("shortcutButtons")),
        "loreBookUrls_count": safe_count(character.get("loreBookUrls")),
        "has_avatar": has_value(character, "avatar"),
        "has_scene_background": scene_metadata["has_scene_background"],
        "has_scene_music": scene_metadata["has_scene_music"],
        "creationTime": character.get("creationTime"),
        "lastMessageTime": character.get("lastMessageTime")
    }


def get_dexie_metadata(data):
    """Returns Dexie/IndexedDB export metadata if the JSON matches Dexie structure."""
    if not isinstance(data, dict):
        return None

    export_data = data.get("data")

    if data.get("formatName") != "dexie":
        return None

    if not isinstance(export_data, dict):
        return None

    if "databaseName" not in export_data or "tables" not in export_data:
        return None

    tables = export_data.get("tables")

    if not isinstance(tables, list):
        return None

    database_name = export_data.get("databaseName")
    classification = "Possible Dexie IndexedDB export"

    if database_name == "chatbot-ui-v1":
        classification = "Perchance AI Character Chat database export"

    table_metadata = []
    character_metadata = []
    exported_rows_by_table = {}

    exported_data = export_data.get("data")

    if isinstance(exported_data, list):
        for exported_table in exported_data:
            if not isinstance(exported_table, dict):
                continue

            table_name = exported_table.get("tableName")
            rows = exported_table.get("rows")

            if table_name and isinstance(rows, list):
                exported_rows_by_table[table_name] = rows

    for table in tables:
        if not isinstance(table, dict):
            continue

        table_name = table.get("name")
        rows = table.get("rows")

        if not isinstance(rows, list):
            rows = exported_rows_by_table.get(table_name)

        actual_rows_length = None

        if isinstance(rows, list):
            actual_rows_length = len(rows)

        table_info = {
            "name": table_name,
            "schema": table.get("schema"),
            "declared_rowCount": table.get("rowCount"),
            "actual_rows_length": actual_rows_length
        }
        table_metadata.append(table_info)

        if table_name == "characters" and isinstance(rows, list):
            for row in rows:
                character_metadata.append(get_safe_character_metadata(row))

    return {
        "classification": classification,
        "formatName": data.get("formatName"),
        "formatVersion": data.get("formatVersion"),
        "databaseName": database_name,
        "databaseVersion": export_data.get("databaseVersion"),
        "table_count": len(tables),
        "tables": table_metadata,
        "characters": character_metadata
    }


def scan_json_file(file_path):
    """
    Safely checks a JSON file.
    Reports whether it is valid JSON and only reports top-level keys.
    """
    result = {
        "json_valid": False,
        "top_level_keys": [],
        "dexie_export": None
    }

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        result["json_valid"] = True
        result["top_level_keys"] = get_top_level_keys(data)
        result["dexie_export"] = get_dexie_metadata(data)

    except Exception:
        result["json_valid"] = False
        result["top_level_keys"] = []
        result["dexie_export"] = None

    return result


def scan_gz_file(file_path):
    """
    Safely checks a gzip file.
    Peeks at a small decompressed text chunk only and does not extract or write files.
    """
    result = {
        "compressed": True,
        "possible_json": False,
        "json_valid": False,
        "top_level_keys": [],
        "dexie_export": None
    }

    try:
        with gzip.open(file_path, "rt", encoding="utf-8", errors="ignore") as file:
            chunk = file.read(512).strip()

        if chunk.startswith("{") or chunk.startswith("["):
            result["possible_json"] = True

            with gzip.open(file_path, "rt", encoding="utf-8", errors="ignore") as file:
                data = json.load(file)

            result["json_valid"] = True
            result["top_level_keys"] = get_top_level_keys(data)
            result["dexie_export"] = get_dexie_metadata(data)

    except Exception:
        result["possible_json"] = False
        result["json_valid"] = False
        result["top_level_keys"] = []
        result["dexie_export"] = None

    return result


def print_dexie_report(dexie_export):
    """Prints safe Dexie/IndexedDB export metadata."""
    if not dexie_export:
        return

    print(f"Dexie Classification: {dexie_export['classification']}")
    print(f"formatName: {dexie_export['formatName']}")
    print(f"formatVersion: {dexie_export['formatVersion']}")
    print(f"databaseName: {dexie_export['databaseName']}")
    print(f"databaseVersion: {dexie_export['databaseVersion']}")
    print(f"Table Count: {dexie_export['table_count']}")

    print("Tables:")
    for table in dexie_export["tables"]:
        print(f"- Name: {table['name']}")
        print(f"  Schema: {table['schema']}")
        print(f"  Declared rowCount: {table['declared_rowCount']}")
        print(f"  Actual exported rows length: {table['actual_rows_length']}")

    if dexie_export["characters"]:
        print("Safe Character Metadata:")

        for character in dexie_export["characters"]:
            print(f"- Character Name: {character['character_name']}")
            print(f"  modelName: {character['modelName']}")
            print(f"  fitMessagesInContextMethod: {character['fitMessagesInContextMethod']}")
            print(f"  autoGenerateMemories: {character['autoGenerateMemories']}")
            print(f"  Has roleInstruction: {character['has_roleInstruction']}")
            print(f"  Has reminderMessage: {character['has_reminderMessage']}")
            print(f"  Has generalWritingInstructions: {character['has_generalWritingInstructions']}")
            print(f"  Has customCode: {character['has_customCode']}")
            print(f"  shortcutButtons count: {character['shortcutButtons_count']}")
            print(f"  loreBookUrls count: {character['loreBookUrls_count']}")
            print(f"  Has avatar: {character['has_avatar']}")
            print(f"  Has scene background: {character['has_scene_background']}")
            print(f"  Has scene music: {character['has_scene_music']}")
            print(f"  creationTime: {character['creationTime']}")
            print(f"  lastMessageTime: {character['lastMessageTime']}")


def scan_project(root_path=None):
    """
    Scans the project for possible Perchance AI Character Chat files.
    Checks the WorldCore AI folder first, then checks the rest of WorldCore.
    Only reports filenames and safe metadata.
    """
    results = []
    scanned_paths = []

    try:
        if root_path is None:
            root_path = get_project_root()

        root_path = os.path.abspath(root_path)
        ai_folder = get_ai_folder()

        # Scan D:\WorldCore\AI first because Perchance files are expected there.
        scan_folder(ai_folder, results, scanned_paths)

        # Then scan the rest of WorldCore as a fallback.
        scan_folder(root_path, results, scanned_paths)

    except Exception:
        return results

    return results


def print_scan_report(results):
    """Prints a safe metadata-only scanner report."""
    print("Perchance AI Character Chat File Scanner")
    print("----------------------------------------")
    print("Purpose: organize future Perchance AI Character Chat files and database-style bundles.")
    print("Network: not used")
    print("Website Access: not used")
    print()

    if not results:
        print("No possible Perchance AI character chat files found.")
        return

    for result in results:
        print(f"File Path: {result['file_path']}")
        print(f"File Type: {result['file_type']}")
        print(f"Possible Purpose: {result['possible_purpose']}")
        print(f"JSON Valid: {result['json_valid']}")
        print(f"Top-Level JSON Keys: {result['top_level_keys']}")
        print(f"Compressed: {result['compressed']}")
        print(f"Possible JSON in GZ: {result['possible_json']}")
        print_dexie_report(result["dexie_export"])
        print()


if __name__ == "__main__":
    scan_results = scan_project()
    print_scan_report(scan_results)
