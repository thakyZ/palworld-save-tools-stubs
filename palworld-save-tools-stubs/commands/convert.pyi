from typing import Literal


def main() -> None: ...


def convert_sav_to_json(
    filename: str,
    output_path: str,
    force: bool = False,
    minify: bool = False,
    allow_nan: bool = True,
    custom_properties_keys: list[str | Literal["all"]] = ["all"],
) -> None : ...


def convert_json_to_sav(filename: str, output_path: str, force: bool = False) -> None: ...


def confirm_prompt(question: str) -> bool: ...
