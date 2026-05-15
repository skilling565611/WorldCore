# ai_image_organizer.py
# Lightweight local image categorization helper for WorldCore AI/IMG.
# This tool reads filenames and folders only. It does not move, rename, delete, upload, or analyze images.

import os


IMAGE_EXTENSIONS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".bmp"
]

CATEGORY_KEYWORDS = {
    "character_image_asset": [
        "character",
        "vixella",
        "rosepaw",
        "judy",
        "kiara",
        "loona",
        "mina",
        "nyra",
        "sienna"
    ],
    "work_evidence_screenshot": [
        "screenshot",
        "vscode",
        "codex",
        "browser",
        "upload"
    ],
    "body_references": [
        "body",
        "pose",
        "full_body",
        "upper_body",
        "lower_body",
        "face",
        "head",
        "hands",
        "feet"
    ],
    "outfit_references": [
        "outfit",
        "clothes",
        "clothing",
        "armor",
        "uniform",
        "dress",
        "style"
    ],
    "scene_rooms": [
        "room",
        "bedroom",
        "bathroom",
        "living",
        "studio",
        "background",
        "scene"
    ],
    "lighting_mood": [
        "light",
        "lighting",
        "mood",
        "night",
        "neon",
        "dramatic",
        "soft"
    ],
    "character_sets": [
        "set",
        "pack",
        "character",
        "sheet",
        "reference"
    ]
}


def get_project_root():
    """Returns the active WorldCore project folder."""
    tools_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(tools_folder)


def get_image_root():
    """Returns the WorldCore AI image folder."""
    return os.path.join(get_project_root(), "AI", "IMG")


def is_image_file(file_name):
    """Returns True if the filename has a known image extension."""
    extension = os.path.splitext(file_name)[1].lower()
    return extension in IMAGE_EXTENSIONS


def guess_category(file_path):
    """Guesses a category from folder and filename text without inspecting image contents."""
    lower_path = file_path.lower().replace("\\", "/")

    for category_id, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in lower_path:
                return category_id

    return "reference_inbox"


def scan_images(root_path=None):
    """
    Scans AI/IMG for image filenames and returns categorization metadata.
    Does not modify files.
    """
    if root_path is None:
        root_path = get_image_root()

    results = []

    try:
        root_path = os.path.abspath(root_path)

        if not os.path.isdir(root_path):
            return results

        for current_folder, folder_names, file_names in os.walk(root_path):
            folder_names[:] = [
                folder_name for folder_name in folder_names
                if folder_name != "__pycache__"
            ]

            for file_name in file_names:
                if not is_image_file(file_name):
                    continue

                file_path = os.path.join(current_folder, file_name)
                results.append({
                    "file_path": file_path,
                    "file_name": file_name,
                    "suggested_category": guess_category(file_path)
                })

    except Exception:
        return results

    return results


def print_image_report(results=None):
    """Prints a local image categorization report."""
    if results is None:
        results = scan_images()

    category_counts = {}

    for item in results:
        category_id = item["suggested_category"]
        category_counts[category_id] = category_counts.get(category_id, 0) + 1

    print("WorldCore AI Image Organization Report")
    print("--------------------------------------")
    print(f"Image Root: {get_image_root()}")
    print(f"Images Found: {len(results)}")
    print()

    print("Category Counts:")
    if not category_counts:
        print("- none")
    else:
        for category_id, count in category_counts.items():
            print(f"- {category_id}: {count}")

    print()
    print("Files:")
    if not results:
        print("No image files found.")
        return

    for item in results:
        print(f"- {item['file_name']}")
        print(f"  Suggested Category: {item['suggested_category']}")
        print(f"  Path: {item['file_path']}")


if __name__ == "__main__":
    print_image_report()
