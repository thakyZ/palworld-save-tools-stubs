from typing import Any, Sequence

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def decode_bytes(
    parent_reader: FArchiveReader, m_bytes: Sequence[int]
) -> dict[str, Any]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...


def encode_bytes(p: dict[str, Any]) -> bytes: ...
