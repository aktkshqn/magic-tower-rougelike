from magic_tower.ui.cui.styles import(
    BOLD,
    RED,
    RESET,
    style_text,
)

def test_style_text_applies_styles():
    result = style_text(
        "魔法の塔",
        BOLD,
        RED,
    )

    assert result == (
        f"{BOLD}{RED}魔法の塔{RESET}"
    )

def test_style_text_without_styles_returns_original_text():
    result = style_text("魔法の塔")

    assert result == "魔法の塔"