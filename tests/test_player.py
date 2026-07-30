from magic_tower.domain.player import(
    normalize_player_name,
    validate_player_name,
)

def test_normalize_player_name_removes_outer_spaces():
    result = normalize_player_name("　アレン　")
    assert result == "アレン"

def test_validate_player_name_accepts_valid_name():
    result = validate_player_name("アレン")

    assert result is None

def test_validate_player_name_rejects_invalid_name():
    result = validate_player_name("")

    assert result == "character.error.empty_name"

def test_validate_player_name_rejects_name_long_name():
    result = validate_player_name("あ" * 13)

    assert result == "character.error.name_too_long"