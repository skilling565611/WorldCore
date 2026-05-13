# cameras.py
# Lightweight fake camera system for WorldCore.
# These are simulated in-world camera feeds only.
# This file does NOT access real webcams, real network cameras, internet streams, or surveillance devices.


# Main fake camera dictionary.
# Each camera is connected to a WorldCore location by location_id.
fake_cameras = {
    "key_cam_01": {
        "display_name": "The Key - Entrance Camera",
        "location_id": "the_key",
        "status": "online",
        "alert_level": "normal",
        "view_description": "Watching the surface entrance and control access point near The Key.",
        "last_scan": "No hostile activity detected."
    },

    "key_cam_02": {
        "display_name": "The Key - Prison Tower Camera",
        "location_id": "the_key",
        "status": "standby",
        "alert_level": "guarded",
        "view_description": "Monitoring the prison tower registration zone and cell access path.",
        "last_scan": "Contained entities remain separated by rank."
    },

    "indian_park_cam_01": {
        "display_name": "Indian Park - Factory Field Camera",
        "location_id": "indian_park",
        "status": "online",
        "alert_level": "stable",
        "view_description": "Watching the factory base field, plant area, and power systems.",
        "last_scan": "Factory base power is restored."
    },

    "indian_park_cam_02": {
        "display_name": "Indian Park - Clone Facility Camera",
        "location_id": "indian_park",
        "status": "online",
        "alert_level": "watch",
        "view_description": "Monitoring clone facility systems and internal base activity.",
        "last_scan": "Clone systems active. No breach confirmed."
    },

    "magic_station_cam_01": {
        "display_name": "Magic Station - Damaged Control Camera",
        "location_id": "magic_station",
        "status": "damaged",
        "alert_level": "unstable",
        "view_description": "Watching the damaged control sensor near the school area.",
        "last_scan": "Signal weak. Maintenance required."
    },

    "reservoir_beach_cam_01": {
        "display_name": "Reservoir Beach - Water Node Camera",
        "location_id": "reservoir_beach",
        "status": "unknown",
        "alert_level": "unknown",
        "view_description": "Monitoring the reservoir/public beach node and water-side systems.",
        "last_scan": "No recent scan data available."
    },

    "home_base_cam_01": {
        "display_name": "Home Base - Power Station Camera",
        "location_id": "home_base",
        "status": "online",
        "alert_level": "normal",
        "view_description": "Watching the main base and local power station connection.",
        "last_scan": "Home base connection stable."
    }
}


def list_cameras():
    """
    Returns a list of all fake camera IDs.
    """
    return list(fake_cameras.keys())


def get_camera(camera_id):
    """
    Returns a fake camera dictionary by camera ID.
    If the camera does not exist, returns None.
    """
    return fake_cameras.get(camera_id)


def set_camera_status(camera_id, new_status):
    """
    Updates the status of a fake camera.
    Returns True if the camera exists and was updated.
    Returns False if the camera does not exist.
    """
    camera = get_camera(camera_id)

    if camera is None:
        return False

    camera["status"] = new_status
    return True


def set_camera_alert(camera_id, new_alert):
    """
    Updates the alert level of a fake camera.
    Returns True if the camera exists and was updated.
    Returns False if the camera does not exist.
    """
    camera = get_camera(camera_id)

    if camera is None:
        return False

    camera["alert_level"] = new_alert
    return True


def print_camera_status():
    """
    Prints a simple overview of all fake camera feeds.
    """
    print("WorldCore Fake Camera Status")
    print("----------------------------")

    for camera_id, data in fake_cameras.items():
        print(f"Camera: {data['display_name']} ({camera_id})")
        print(f"Location: {data['location_id']}")
        print(f"Status: {data['status']}")
        print(f"Alert: {data['alert_level']}")
        print(f"View: {data['view_description']}")
        print(f"Last Scan: {data['last_scan']}")
        print()


# Simple test area.
# This only runs when this file is opened directly.
if __name__ == "__main__":
    print_camera_status()

    print("Camera IDs:")
    print(list_cameras())
    print()

    print("Updating Magic Station camera...")
    updated = set_camera_status("magic_station_cam_01", "repair_pending")

    if updated:
        print("Magic Station camera status updated successfully.")
    else:
        print("Camera was not found.")

    print()
    print_camera_status()
