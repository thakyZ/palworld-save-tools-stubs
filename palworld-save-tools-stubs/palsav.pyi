#!/usr/bin/env python3


from typing import Literal

MAGIC_BYTES: Literal[b"Plz"]


def decompress_sav_to_gvas(data: bytes) -> tuple[bytes, int]: ...


def compress_gvas_to_sav(data: bytes, save_type: int) -> bytes: ...
