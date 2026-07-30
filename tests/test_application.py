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

from magic_tower.application import (
    wait_for_title_choice,
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