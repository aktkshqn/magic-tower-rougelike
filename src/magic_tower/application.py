from .data.scenes import INTRO_SCENES

def play_scene(ui, scenes):
    for scene in scenes:
        ui.render_scene(scene)

def wait_for_title_choice(ui):
    while True:
        raw_value = ui.receive_input(
            "menu.prompt.select"
        )

        if raw_value in {"1", "2"}:
            return int(raw_value)

        ui.render_message(
            "menu.error.invalid_choice"
        )

def run_game(ui):
    ui.play_scenes(
        ui,
        INTRO_SCENES
    )
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

