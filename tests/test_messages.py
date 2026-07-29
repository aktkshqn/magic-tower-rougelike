import pytest

from magic_tower.data.messages import get_message


def test_get_message_returns_fixed_message():
    result = get_message("game.info.start")

    assert result == "新しい冒険を始めます。"


def test_get_message_inserts_values():
    result = get_message(
        "combat.result.damage",
        attacker="アレン",
        target="スライム",
        damage=8,
    )

    assert result == "アレンはスライムに8のダメージ！"


def test_get_message_rejects_unknown_key():
    with pytest.raises(KeyError):
        get_message("unknown.message")
