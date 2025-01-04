from color_contrast import check_contrast, AccessibilityLevel
from utils.ThemeReplacer import REPLACEMENTS


def main() -> None:
    BACKGROUND = REPLACEMENTS["{{BACKGROUND}}"]

    # remove unnecessary keys to check contrast
    keys_to_remove = [
        "{{BACKGROUND}}",
        "{{FOREGROUND}}",
        "{{INFO_DARKEN}}",
        "{{GIT_IGNORED}}",
    ]

    for key in keys_to_remove:
        REPLACEMENTS.pop(key)

    # loop through all values in the dictionary
    for key, value in REPLACEMENTS.items():
        is_valid = check_contrast(value, BACKGROUND, level=AccessibilityLevel.AA)
        if not is_valid:
            print(f"{key} fails contrast check.")


if __name__ == "__main__":
    main()
