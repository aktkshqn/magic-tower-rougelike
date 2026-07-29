def run_game(ui):
    ui.play_intro()
    ui.show_title()

    choice = ui.select_title_menu()

    if choice == 1:
        ui.show_system_message(
            "game.info.start"
        )
    else:
        ui.show_system_message(
            "game.info.exit"
        )