import time

from magic_tower import cui


def test_show_message_displays_text(capsys, monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda seconds: None)

    cui.show_message("魔法の塔", speed=0.05)

    captured = capsys.readouterr()

    assert captured.out == "魔法の塔\n"


def test_select_title_menu_returns_start(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "1")

    result = cui.select_title_menu()

    assert result == 1


def test_select_title_menu_retries_invalid_input(
    capsys,
    monkeypatch,
):
    answers = iter(["abc", "1"])
    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(answers),
    )

    result = cui.select_title_menu()
    captured = capsys.readouterr()

    assert result == 1
    assert "表示された番号から選んでください。" in captured.out
