import os
import time

from .cui_assets import TITLE_ART
from .cui_styles import BOLD, RED,style_text
from .messages import get_message

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_message(message, speed=0.05):
    for character in message:
        print(character, end="", flush=True)
        time.sleep(speed)

    print()

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



def show_title():
    clear_screen()

    print("\a", end="", flush=True)

    decorated_title = style_text(TITLE_ART, BOLD, RED)

    print(decorated_title)
    time.sleep(3)