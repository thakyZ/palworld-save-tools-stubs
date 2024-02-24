#!/usr/bin/env python3


#pyright: reportMissingTypeStubs=false

from typing import Any, Sequence, Optional

from palworld_save_tools.archive import *


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def connect_info_item_reader(reader: FArchiveReader) -> dict[str, Any]: ...


def connect_info_item_writer(writer: FArchiveWriter, properties: dict[str, Any]) -> None: ...


def decode_bytes(
    parent_reader: FArchiveReader, c_bytes: Sequence[int]
) -> Optional[dict[str, Any]]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...


def encode_bytes(p: dict[str, Any]) -> bytes: ...
