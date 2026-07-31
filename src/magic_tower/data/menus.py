from magic_tower.domain.menu import (
    MenuDefinition,
    MenuOption,
)

TITLE_MENU = MenuDefinition(
    id="title",
    prompt_key="menu.prompt.select",
    options=(
        MenuOption(
            id="start",
            label_key="menu.option.start",
            result_id="game.start",
        ),
        MenuOption(
            id="exit",
            label_key="menu.option.exit",
            result_id="game.exit",
        ),
    )
)
