class FakeUI:
    def __init__(self, inputs):
        self.inputs = iter(inputs)
        self.events = []

    def receive_input(self, prompt_key):
        self.events.append(
            ("input", prompt_key)
        )

        return next(self.inputs)

    def render_message(
        self,
        message_key,
        **values,
    ):
        self.events.append(
            ("message", message_key, values)
        )

    def render_scene(self, scene):
        self.events.append(
            ("scene", scene)
        )

from magic_tower.application import (
    wait_for_title_choice,
    play_scenes,
)

def test_wait_for_title_choice_returns_invalid_input():
    ui = FakeUI(["abc", "1"])

    result = wait_for_title_choice(ui)

    assert result == 1
    assert ui.events == [
        ("input", "menu.prompt.select"),
        (
            "message", 
            "menu.error.invalid_choice", 
            {}
        ),
        ("input", "menu.prompt.select"),
    ]

def test_play_scenes_renders_scenes_in_order():
    ui = FakeUI([])
    scenes = [
        {"id": "intro.first"},
        {"id": "intro.second"},
    ]

    play_scenes(ui, scenes)

    assert ui.events == [
        ("scene", {"id": "intro.first"}),
        ("scene", {"id": "intro.second"}),
    ]