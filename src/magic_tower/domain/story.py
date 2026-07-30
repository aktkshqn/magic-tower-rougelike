from dataclasses import dataclass

@dataclass(frozen=True)
class SceneSequence:
    id: str
    scene_ids: tuple[str, ...]
    next_sequence_id: str | None = None
    menu_id: str | None = None
    is_terminal: bool = False

@dataclass(frozen=True)
class MenuOption:
    id: str
    lable_key: str
    target_sequence_id: str
    confirmation_key: str | None = None

@dataclass(frozen=True)
class MenuDefinition:
    id: str
    prompt_key: str
    options: tuple[MenuOption, ...]
    invalid_choice_key: str
    require_confirmation: bool = False
    confirmation_prompt_key: str = "menu.confirm.selected"
    confirmation_accept_key: str = "menu.confirm.yes"
    confirmation_reject_key: str = "menu.confirm.no"