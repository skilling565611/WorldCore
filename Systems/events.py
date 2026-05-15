# events.py
# Lightweight WorldCore event log system.
# Tracks important world activity without using a database.

from datetime import datetime


event_log = []

# Known event categories for simple organization.
# add_event currently stores any category text it receives so older/free-form logs still work.
# Validation may be added later if WorldCore needs stricter event data.
event_categories = [
    "system",
    "threat",
    "power",
    "base",
    "shield",
    "transport",
    "camera"
]


def add_event(title, category, location_id, description):
    """
    Adds a new event to the WorldCore event log.
    Returns the created event dictionary.

    TODO: Decide later whether category should be validated against event_categories.
    """
    event_id = len(event_log) + 1

    event = {
        "id": event_id,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "title": title,
        "category": category,
        "location_id": location_id,
        "description": description
    }

    event_log.append(event)
    return event


def add_system_event(title, description):
    """Adds a system event."""
    return add_event(title, "system", "worldcore", description)


def add_threat_event(title, location_id, description):
    """Adds a threat event."""
    return add_event(title, "threat", location_id, description)


def add_power_event(title, location_id, description):
    """Adds a power event."""
    return add_event(title, "power", location_id, description)


def list_events():
    """Returns all events."""
    return event_log


def clear_events():
    """Clears all events from the event log."""
    event_log.clear()
    return True


def get_events_by_category(category):
    """Returns events matching a category."""
    return [
        event for event in event_log
        if event["category"] == category
    ]


def get_events_by_location(location_id):
    """Returns events matching a location ID."""
    return [
        event for event in event_log
        if event["location_id"] == location_id
    ]


def print_event_log():
    """Prints all events in the event log."""
    print("WorldCore Event Log")
    print("-------------------")

    if not event_log:
        print("No events recorded.")
        return

    for event in event_log:
        print(f"ID: {event['id']}")
        print(f"Time: {event['timestamp']}")
        print(f"Title: {event['title']}")
        print(f"Category: {event['category']}")
        print(f"Location: {event['location_id']}")
        print(f"Description: {event['description']}")
        print()


if __name__ == "__main__":
    add_event(
        title="WorldCore Foundation Started",
        category="system",
        location_id="worldcore",
        description="Initial WorldCore foundation modules are being created."
    )

    add_event(
        title="The Key Returned Online",
        category="base",
        location_id="the_key",
        description="The Key base is active and ready for prison tower mode."
    )

    add_event(
        title="Mystery Man Clone Detection",
        category="threat",
        location_id="indian_park",
        description="Possible Mystery Man clone activity detected near the factory base."
    )

    print_event_log()
