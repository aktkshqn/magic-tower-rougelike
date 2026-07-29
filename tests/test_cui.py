import time

from magic_tower.ui.cui import adapter


def test_show_message_displays_text(capsys, monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda seconds: None)

    adapter.show_message("魔法の塔", speed=0.05)

    captured = capsys.readouterr()

    assert captured.out == "魔法の塔\n"

def test_play_scene_displays_all_lines(
    capsys,
    monkeypatch,
):
    monkeypatch.setattr(
        adapter.time,
        "sleep",
        lambda seconds: None,
    )

    scene = {
        "lines": ["一行目", "二行目"],
        "speed": 0,
        "wait": 0,
        "clear": False,
    }

    adapter.play_scene(scene)

    captured = capsys.readouterr()

    assert captured.out == "一行目\n二行目\n"


def test_select_title_menu_returns_start(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "1")

    result = adapter.select_title_menu()

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

    result = adapter.select_title_menu()
    captured = capsys.readouterr()

    assert result == 1
    assert "表示された番号から選んでください。" in captured.out
