#!/usr/bin/env python3


#pyright: reportMissingTypeStubs=false

from typing import Any

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter


def pal_item_and_num_read(reader: FArchiveReader) -> dict[str, Any]: ...


def pal_item_and_slot_writer(writer: FArchiveWriter, p: dict[str, Any]) -> None: ...
