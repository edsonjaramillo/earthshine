from pathlib import Path
from utils.ThemeReplacer import ThemeReplacer


class VSCodeBuilder:
    @staticmethod
    def build():
        vs_code_template = Path("themes/earthshine-vscode/templates/template-vscode-theme.json")
        vs_code_theme = Path("themes/earthshine-vscode/themes/Earthshine-color-theme.json")
        vscode_tr = ThemeReplacer()
        vscode_tr.replace_template(vs_code_template, vs_code_theme)
        vscode_tr.prettify_json(vs_code_theme)
