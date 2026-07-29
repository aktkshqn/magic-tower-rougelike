import time

from .scene_data import INTRO_SCENES
from . import cui

def play_intro():
    for scene in INTRO_SCENES:
        play_scene(scene)


def play_scene(scene):
    for line in scene["lines"]:
        cui.show_message(line, scene["speed"])

    time.sleep(scene["wait"])

    if scene["clear"]:
        cui.clear_screen()

def main():
    play_intro()
    cui.show_title()
    choice = cui.select_title_menu()

    if choice == 1:
        print("ゲームを開始します。")  
    else:
        print("ゲームを終了します。")


if __name__ == "__main__":
    main()