from magic_tower import main
from magic_tower.messages import get_message

def test_select_title_menu_returns_start(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "1")

    result = main.select_title_menu()

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

    result = main.select_title_menu()
    captured = capsys.readouterr()

    expected_message = get_message("menu.error.invalid_choice")

    assert result == 1
    assert expected_message in captured.out