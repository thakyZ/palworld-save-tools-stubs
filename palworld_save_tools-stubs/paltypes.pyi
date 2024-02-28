# pyright: reportArgumentType=false
# pylint: disable=C0114,C0301

from typing import Any, Callable, Literal

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter

from ..palworld_save_tools_stubs.archive import PalworldTypeHints, PalworldCustomProperties

PALWORLD_TYPE_HINTS: PalworldTypeHints

PALWORLD_CUSTOM_PROPERTIES: PalworldCustomProperties
