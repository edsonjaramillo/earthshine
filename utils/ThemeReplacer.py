from pathlib import Path
import json

REPLACEMENTS = {
    "{{BACKGROUND}}": "#000000",
    "{{FOREGROUND}}": "#141414",
    "{{NEUTRAL}}": "#b8b8b8",
    "{{WHITE}}": "#fafafa",
    "{{INFO}}": "#1f72f1",
    "{{INFO_DARKEN}}": "#1b418d",
    "{{ERROR}}": "#e03838",
    "{{WARNING}}": "#f57c00",
    "{{GIT_ADDED}}": "#4ade80",
    "{{GIT_MODIFIED}}": "#f8c730",
    "{{GIT_DELETED}}": "#ee3a3a",
    "{{GIT_CONFLICT}}": "#6f6fd1",
    "{{GIT_IGNORED}}": "#656565",
    "{{MISC_TOKENS}}": "#abb2bf",
    "{{VARIABLE_PROPS}}": "#ee6e6c",
    "{{KEYWORDS}}": "#dd72fa",
    "{{NUMBERS}}": "#f28f36",
    "{{CLASSES_CONSTANTS}}": "#f3c80f",
    "{{FUNCTIONS}}": "#65a0fc",
    "{{STRINGS}}": "#66dc7e",
    "{{OPERATORS}}": "#4bd0ee",
    "{{COMMENTS}}": "#7f848e",
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
