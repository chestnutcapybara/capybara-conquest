from pathlib import Path
import sys

def resolve_path(relative_path: str) -> Path:
    if getattr(sys, "frozen", False):
        base_path = Path(sys.argv[0]).resolve().parent
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path

class LoadAssets:
    pass