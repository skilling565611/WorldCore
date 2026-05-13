# ai_system.py
# Lightweight WorldCore AI organization settings.
# No real AI model calls, networking, APIs, or external links are used here.

ai_system = {
    "display_name": "WorldCore AI Layer",
    "status": "local_organization_only",
    "ai_link_enabled": False,
    "ai_link_target": "Control Prime",
    "current_shell": "Arctic Prime",
    "notes": (
        "This module organizes local AI-related data for WorldCore. "
        "The real AI link is intentionally left disabled until Control Prime."
    )
}

image_categories = {
    "character_references": {
        "display_name": "Character References",
        "folder_hint": "AI/IMG/Character_References",
        "purpose": "Main character images, design references, and identity anchors."
    },
    "body_references": {
        "display_name": "Body References",
        "folder_hint": "AI/IMG/Adult_Only/Body_References",
        "purpose": "Body reference categories for later manual organization."
    },
    "outfit_references": {
        "display_name": "Outfit References",
        "folder_hint": "AI/IMG/Adult_Only/Outfit_References",
        "purpose": "Clothing, armor, uniforms, and style references."
    },
    "scene_rooms": {
        "display_name": "Scene Rooms",
        "folder_hint": "AI/IMG/Adult_Only/Scene_Rooms",
        "purpose": "Room, background, and setting references."
    },
    "lighting_mood": {
        "display_name": "Lighting and Mood",
        "folder_hint": "AI/IMG/Adult_Only/Lighting_Mood",
        "purpose": "Lighting, color mood, and atmosphere references."
    },
    "character_sets": {
        "display_name": "Character Sets",
        "folder_hint": "AI/IMG/Adult_Only/Character_Sets",
        "purpose": "Grouped images for one character or character pack."
    },
    "reference_inbox": {
        "display_name": "Reference Inbox",
        "folder_hint": "AI/IMG/Adult_Only/Reference_Inbox",
        "purpose": "Temporary place for unsorted images."
    }
}


def get_ai_system():
    """Returns the AI system settings."""
    return ai_system


def list_image_categories():
    """Returns all local image category IDs."""
    return list(image_categories.keys())


def get_image_category(category_id):
    """Returns image category data by ID, or None if not found."""
    return image_categories.get(category_id)


def is_ai_link_enabled():
    """Returns whether the future real AI link is enabled."""
    return ai_system["ai_link_enabled"]


def print_ai_status():
    """Prints the current WorldCore AI organization status."""
    print("WorldCore AI Status")
    print("-------------------")
    print(f"Display Name: {ai_system['display_name']}")
    print(f"Status: {ai_system['status']}")
    print(f"AI Link Enabled: {ai_system['ai_link_enabled']}")
    print(f"AI Link Target: {ai_system['ai_link_target']}")
    print(f"Current Shell: {ai_system['current_shell']}")
    print(f"Notes: {ai_system['notes']}")
    print()

    print("Image Categories:")
    for category_id, data in image_categories.items():
        print(f"- {data['display_name']} ({category_id})")
        print(f"  Folder Hint: {data['folder_hint']}")
        print(f"  Purpose: {data['purpose']}")


if __name__ == "__main__":
    print_ai_status()
