# perchance_schema_helper.py
# Lightweight Perchance AI Character Chat schema helper for WorldCore.
# Stores known field meanings and validates safe metadata only.

PERCHANCE_CHARACTER_FIELDS = {
    "name": "Character display name.",
    "roleInstruction": "Main private character behavior instruction. Do not print full value.",
    "reminderMessage": "Reminder/context message for the character. Do not print full value.",
    "generalWritingInstructions": "General writing style instructions. Do not print full value.",
    "messageWrapperStyle": "Formatting style for character messages.",
    "imagePromptPrefix": "Prefix added to image prompts. Do not print full value.",
    "imagePromptSuffix": "Suffix added to image prompts. Do not print full value.",
    "imagePromptTriggers": "Trigger rules for image prompts.",
    "initialMessages": "Starter messages for new chats. Count only.",
    "shortcutButtons": "Quick action buttons for the character. Count only.",
    "loreBookUrls": "Linked lore books. Count only; do not print URLs.",
    "avatar": "Character avatar/media reference. Report existence only.",
    "scene": "Scene settings such as background and music. Report existence only.",
    "customCode": "Custom JavaScript/code behavior. Report existence only; do not print code.",
    "customData": "Extra custom metadata for the character.",
    "modelName": "Selected AI model name.",
    "temperature": "Generation randomness setting.",
    "maxTokensPerMessage": "Maximum output tokens per message.",
    "fitMessagesInContextMethod": "How old messages are handled when context is full.",
    "autoGenerateMemories": "Memory generation setting."
}

PERCHANCE_THREAD_FIELDS = {
    "id": "Thread database ID.",
    "name": "Thread name.",
    "characterId": "Linked character ID.",
    "creationTime": "Thread creation timestamp.",
    "lastMessageTime": "Most recent message timestamp.",
    "lastViewTime": "Most recent view timestamp.",
    "folderPath": "Folder path label."
}

PERCHANCE_MESSAGE_FIELDS = {
    "id": "Message database ID.",
    "threadId": "Linked thread ID.",
    "characterId": "Linked character ID.",
    "creationTime": "Message creation timestamp.",
    "order": "Message order inside the thread.",
    "content": "Message content. Do not print full value.",
    "role": "Message role, such as user or assistant."
}

PERCHANCE_CUSTOM_CODE_FEATURES = {
    "message_hooks": "Custom behavior that may adjust message flow.",
    "button_actions": "Custom behavior connected to shortcut buttons.",
    "scene_controls": "Custom behavior that may update scene state.",
    "memory_helpers": "Custom behavior that may support memory or context features.",
    "ui_helpers": "Custom behavior that may affect display or interaction."
}


def list_character_fields():
    """Returns all known Perchance character field names."""
    return list(PERCHANCE_CHARACTER_FIELDS.keys())


def explain_field(field_name):
    """Returns a short explanation for a known field, or None if unknown."""
    if field_name in PERCHANCE_CHARACTER_FIELDS:
        return PERCHANCE_CHARACTER_FIELDS[field_name]

    if field_name in PERCHANCE_THREAD_FIELDS:
        return PERCHANCE_THREAD_FIELDS[field_name]

    if field_name in PERCHANCE_MESSAGE_FIELDS:
        return PERCHANCE_MESSAGE_FIELDS[field_name]

    if field_name in PERCHANCE_CUSTOM_CODE_FEATURES:
        return PERCHANCE_CUSTOM_CODE_FEATURES[field_name]

    return None


def has_safe_value(data, field_name):
    """Returns True when a field exists and has a non-empty value."""
    if not isinstance(data, dict):
        return False

    value = data.get(field_name)

    if value is None:
        return False

    if value == "":
        return False

    if value == []:
        return False

    if value == {}:
        return False

    return True


def safe_count(value):
    """Returns a safe count for lists and dictionaries."""
    if isinstance(value, list):
        return len(value)

    if isinstance(value, dict):
        return len(value)

    if value:
        return 1

    return 0


def get_scene_status(character_data):
    """Returns safe scene background/music existence flags."""
    scene = character_data.get("scene")

    if not isinstance(scene, dict):
        scene = {}

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

    has_background = False
    has_music = False

    for key in background_keys:
        if has_safe_value(character_data, key) or has_safe_value(scene, key):
            has_background = True

    for key in music_keys:
        if has_safe_value(character_data, key) or has_safe_value(scene, key):
            has_music = True

    return {
        "scene_background_exists": has_background,
        "scene_music_exists": has_music
    }


def validate_character_metadata(character_data):
    """
    Validates safe Perchance character metadata.
    Does not return or print full prompts, custom code, URLs, secrets, or message contents.
    """
    if not isinstance(character_data, dict):
        return {
            "valid_input": False,
            "error": "character_data must be a dictionary"
        }

    scene_status = get_scene_status(character_data)

    return {
        "valid_input": True,
        "character_name_exists": has_safe_value(character_data, "name"),
        "roleInstruction_exists": has_safe_value(character_data, "roleInstruction"),
        "reminderMessage_exists": has_safe_value(character_data, "reminderMessage"),
        "generalWritingInstructions_exists": has_safe_value(character_data, "generalWritingInstructions"),
        "customCode_exists": has_safe_value(character_data, "customCode"),
        "shortcutButtons_count": safe_count(character_data.get("shortcutButtons")),
        "loreBookUrls_count": safe_count(character_data.get("loreBookUrls")),
        "avatar_exists": has_safe_value(character_data, "avatar"),
        "scene_background_exists": scene_status["scene_background_exists"],
        "scene_music_exists": scene_status["scene_music_exists"],
        "initialMessages_count": safe_count(character_data.get("initialMessages"))
    }


def print_schema_summary():
    """Prints a safe summary of known Perchance schema fields."""
    print("Perchance Character Schema Helper")
    print("---------------------------------")
    print(f"Character Fields: {len(PERCHANCE_CHARACTER_FIELDS)}")
    print(f"Thread Fields: {len(PERCHANCE_THREAD_FIELDS)}")
    print(f"Message Fields: {len(PERCHANCE_MESSAGE_FIELDS)}")
    print(f"Custom Code Feature Groups: {len(PERCHANCE_CUSTOM_CODE_FEATURES)}")
    print()

    print("Character Fields")
    print("----------------")
    for field_name, description in PERCHANCE_CHARACTER_FIELDS.items():
        print(f"- {field_name}: {description}")


if __name__ == "__main__":
    print_schema_summary()
