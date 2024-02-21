#!/usr/bin/env python3


#pyright: reportMissingTypeStubs=false

from typing import Any, Sequence

from palworld_save_tools.archive import FArchiveWriter, FArchiveReader


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def decode_bytes(
    parent_reader: FArchiveReader, b_bytes: Sequence[int]
) -> dict[str, Any]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...


def encode_bytes(p: dict[str, Any]) -> bytes: ...
