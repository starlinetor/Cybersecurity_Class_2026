import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    """Load json file

    Args:
        path (Path): json file path

    Returns:
        Any: json object
    """
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)