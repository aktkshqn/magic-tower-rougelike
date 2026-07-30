MAX_PLAYER_NAME_LENGTH = 12


def normalize_player_name(raw_name):
    return raw_name.strip()


def validate_player_name(player_name):
    if not player_name:
        return "character.error.empty_name"

    if len(player_name) > MAX_PLAYER_NAME_LENGTH:
        return "character.error.name_too_long"

    return None