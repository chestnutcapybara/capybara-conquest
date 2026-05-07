from pathlib import Path
from typing import Any
import sys
def resolve_path(relative_path: str) -> Path:
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(getattr(sys, "_MEIPASS"))
    else:
        # In development, use the current working directory
        base_path = Path(".").resolve()

    return base_path / Path(relative_path)

class LoadAssets:
    pass