# access_levels.py
# Lightweight WorldCore access level system.
# Supports A1 through Z10, plus God-level access above normal ranks.


# Rank classes from lowest to highest normal access.
# Normal ranks advance A1-A10, then B1-B10, continuing through Z10.
# Current control logic is class-first: B1 outranks A10, and Z10 is the top normal rank.
# God-tier ranks sit above all A-Z ranks and are intentionally kept separate.
rank_classes = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]


def get_rank_value(rank_class):
    """
    Returns the numeric value of a rank class.
    A is lowest. Z is highest normal rank.
    Returns None if the rank class is invalid.
    """
    rank_class = rank_class.upper()

    if rank_class not in rank_classes:
        return None

    return rank_classes.index(rank_class) + 1


def parse_access_level(access_level):
    """
    Parses an access level like A10, B1, Z10, or God5.
    Returns a dictionary with rank_type, rank_class, and level.
    """
    access_level = access_level.strip()

    if access_level.lower().startswith("god"):
        level_text = access_level[3:]

        if level_text == "":
            level = 1
        else:
            level = int(level_text)

        return {
            "rank_type": "god",
            "rank_class": "GOD",
            "level": level
        }

    rank_class = access_level[0].upper()
    level = int(access_level[1:])

    return {
        "rank_type": "normal",
        "rank_class": rank_class,
        "level": level
    }


def can_control_rank(user_rank, target_rank):
    """
    Checks if user_rank can control target_rank.

    Rules:
    - God tier controls all normal ranks.
    - Higher rank classes control lower rank classes before numeric level is checked.
    - Same rank class requires level 10 for full control.
    - Lower rank classes cannot control higher rank classes.
    """
    user = parse_access_level(user_rank)
    target = parse_access_level(target_rank)

    if user["rank_type"] == "god":
        return True

    if target["rank_type"] == "god":
        return False

    user_value = get_rank_value(user["rank_class"])
    target_value = get_rank_value(target["rank_class"])

    if user_value is None or target_value is None:
        return False

    if user_value > target_value:
        return True

    if user_value == target_value and user["level"] == 10:
        return True

    return False


def print_access_examples():
    """Prints example access checks for the current class-first rank logic."""
    examples = [
        ("A10", "A1"),
        ("A10", "B1"),
        ("B1", "A10"),
        ("Z10", "A1"),
        ("God1", "Z10"),
        ("A1", "A10")
    ]

    print("WorldCore Access Level Examples")
    print("-------------------------------")

    for user_rank, target_rank in examples:
        result = can_control_rank(user_rank, target_rank)
        print(f"{user_rank} can control {target_rank}: {result}")


if __name__ == "__main__":
    print_access_examples()
