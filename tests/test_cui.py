import time

from magic_tower.ui.cui import adapter


def test_render_message_displays_text(capsys, monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda seconds: None)

    adapter.render_message("魔法の塔", speed=0.05)

    captured = capsys.readouterr()

    assert captured.out == "魔法の塔\n"

def test_render_scene_displays_all_lines(
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

    adapter.render_scene(scene)

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

def test_receive_input_returns_user_input(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt:"1",
    )

    result = adapter.receive_input(
        "menu.prompt.select"
    )

    assert result == "1"