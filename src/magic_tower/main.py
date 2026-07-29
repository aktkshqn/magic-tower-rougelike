import os
import time

from .scene_data import INTRO_SCENES, TITLE_ART
from .cui import select_title_menu, show_message, clear_screen

RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"

def play_scene(scene):
    for line in scene["lines"]:
        show_message(line, scene["speed"])

    time.sleep(scene["wait"])

    if scene["clear"]:
        clear_screen()


def play_intro():
    for scene in INTRO_SCENES:
        play_scene(scene)


def show_title():
    clear_screen()

    print("\a", end="", flush=True)
    print(f"{BOLD}{RED}{TITLE_ART}{RESET}")

    time.sleep(3)

def main():
    play_intro()
    show_title()
    choice = select_title_menu()

    if choice == 1:
        print("ゲームを開始します。")  
    else:
        print("ゲームを終了します。")


if __name__ == "__main__":
    main()