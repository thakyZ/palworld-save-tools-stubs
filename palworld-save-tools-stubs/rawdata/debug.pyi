from typing import Any

from palworld_save_tools.archive import *


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...
