from magic_tower import main


def test_show_message_displays_text(capsys, monkeypatch):
    monkeypatch.setattr(main.time, "sleep", lambda seconds: None)

    main.show_message("魔法の塔", speed=0.05)

    captured = capsys.readouterr()

    assert captured.out == "魔法の塔\n"

def test_select_title_menu_returns_start(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "1")

    result = main.select_title_menu()

    assert result == "1"

def test_select_title_menu_retries_invalid_input(
    capsys,
    monkeypatch,
):
    answers = iter(["abc", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(answers),
    )

    result = main.select_title_menu()
    captured = capsys.readouterr()

    assert result == "1"
    assert "1か2を入力してください。" in captured.out