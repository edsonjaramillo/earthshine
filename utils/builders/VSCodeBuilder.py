from pathlib import Path
from utils.ThemeReplacer import ThemeReplacer


class VSCodeBuilder:
    @staticmethod
    def build():
        VS_CODE_TEMPLATE = Path("vscode/templates/base.json")
        VS_CODE_THEMES = Path("vscode/themes/Earthshine-color-theme.json")
        vscode_tr = ThemeReplacer()
        vscode_tr.replace_template(VS_CODE_TEMPLATE, VS_CODE_THEMES)
        vscode_tr.prettify_json(VS_CODE_THEMES)
