RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"


def style_text(text, *styles):
    if not styles:
        return text

    style_codes = "".join(styles)

    return f"{style_codes}{text}{RESET}"