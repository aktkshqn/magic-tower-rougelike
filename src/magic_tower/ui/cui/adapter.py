import os
import time

from ...assets.ascii_art import TITLE_ART
from ...data.messages import get_message
from .styles import BOLD, BLUE,style_text

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def render_scene(scene):
    for line in scene["lines"]:
        render_message(
            line,
            scene["speed"],
        )

    time.sleep(scene["wait"])

    if scene["clear"]:
        clear_screen()

def render_message(message, speed=0.05):
    for character in message:
        print(character, end="", flush=True)
        time.sleep(speed)

    print()

def show_title():
    clear_screen()

    print("\a", end="", flush=True)

    decorated_title = style_text(TITLE_ART, BOLD, BLUE)

    print(decorated_title)
    time.sleep(3)

def select_title_menu():
    while True:
        choice = input(
            get_message("menu.prompt.select")
        )

        if choice in {"1", "2"}:
            return int(choice)

        print(
            get_message("menu.error.invalid_choice")
        )

def show_system_message(message_key, **values):
    message = get_message(message_key, **values)
    render_message(message)

def receive_input(prompt_key):
    prompt = get_message(prompt_key)

    return input(prompt)
