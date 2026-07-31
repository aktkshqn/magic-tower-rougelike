from magic_tower.data.menus import TITLE_MENU

def test_title_menu_has_start_and_exit_option():
    assert len(TITLE_MENU.options) == 2

    assert TITLE_MENU.options[0].result_id == (
        "game.start"
    )
    assert TITLE_MENU.options[1].result_id == (
        "game.exit"
    )