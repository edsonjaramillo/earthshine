from pathlib import Path
import json

REPLACEMENTS = {
    # Grayscale Palette
    "{{BACKGROUND}}": "#030303",
    "{{FOREGROUND}}": "#141414",
    "{{NEUTRAL_DARK}}": "#787878",
    "{{NEUTRAL}}": "#aeaeae",
    "{{NEUTRAL_LIGHT}}": "#e8e8e8",
    # Color Palette
    "{{BLACK}}": "#030303",
    "{{BLUE}}": "#409cff",
    "{{CYAN}}": "#00d0df",
    "{{GREEN}}": "#24d064",
    "{{MAGENTA}}": "#f278e8",
    "{{PURPLE}}": "#a272fe",
    "{{RED}}": "#e35659",
    "{{WHITE}}": "#fafafa",
    "{{ORANGE}}": "#ed914b",
    "{{YELLOW}}": "#f8cc5a",
    # Bright Color Palette
    "{{BRIGHT_BLACK}}": "#404040",
    "{{BRIGHT_BLUE}}": "#3d73eb",
    "{{BRIGHT_CYAN}}": "#0891b2",
    "{{BRIGHT_GREEN}}": "#16a34a",
    "{{BRIGHT_MAGENTA}}": "#f52c85",
    "{{BRIGHT_PURPLE}}": "#a57de8",
    "{{BRIGHT_RED}}": "#f62a2a",
    "{{BRIGHT_WHITE}}": "#f5f5f5",
    "{{BRIGHT_ORANGE}}": "#f28f36",
    "{{BRIGHT_YELLOW}}": "#eab308",
}


class ThemeReplacer:
    def replace_template(self, template_path: Path, output_path: Path):
        """
        Replace placeholders in the template file with actual values and save the result to the output file.

        :param template_path: Path to the template file
        :param output_path: Path to save the processed file
        """
        self._verify_file_exists(template_path)

        with template_path.open("r") as file:
            content = file.read()

        for key, value in REPLACEMENTS.items():
            content = content.replace(key, value)

        with output_path.open("w") as file:
            file.write(content)

    def _verify_file_exists(self, file_path: Path):
        """
        Verify that the file exists.

        :param file_path: Path to the file to verify
        :raises FileNotFoundError: If the file does not exist
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")

    def prettify_json(self, file_path: Path):
        """
        Prettify the JSON file by formatting it with an indentation of 2 spaces.

        :param file_path: Path to the JSON file to prettify
        """
        with file_path.open("r") as file:
            data = json.load(file)

        with file_path.open("w") as file:
            json.dump(data, file, indent=2)
