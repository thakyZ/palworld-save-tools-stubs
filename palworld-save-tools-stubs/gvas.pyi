#!/usr/bin/env python3

# pyright: reportMissingTypeStubs=false

from typing import Any

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter, UUID

from paltypes import PalworldTypeHints, PalworldCustomProperties

def custom_version_reader(reader: FArchiveReader) -> tuple[UUID, int]: ...

def custom_version_writer(writer: FArchiveWriter, value: tuple[str, int]) -> None: ...

class GvasHeader:
    magic: int
    save_game_version: int
    package_file_version_ue4: int
    package_file_version_ue5: int
    engine_version_major: int
    engine_version_minor: int
    engine_version_patch: int
    engine_version_changelist: int
    engine_version_branch: str
    custom_version_format: int
    custom_versions: list[tuple[str, int]]
    save_game_class_name: str

    @staticmethod
    def read(reader: FArchiveReader) -> "GvasHeader": ...
    @staticmethod
    def load(dict: dict[str, Any]) -> "GvasHeader": ...
    def dump(self) -> dict[str, Any]: ...
    def write(self, writer: FArchiveWriter) -> None: ...

class GvasFile:
    header: GvasHeader
    properties: dict[str, Any]
    trailer: bytes

    @staticmethod
    def read(
        data: bytes,
        type_hints: PalworldTypeHints = {},
        custom_properties: PalworldCustomProperties = {},
        allow_nan: bool = True,
    ) -> "GvasFile": ...
    @staticmethod
    def load(dict: dict[str, Any]) -> "GvasFile": ...
    def dump(self) -> dict[str, Any]: ...
    def write(self, custom_properties: PalworldCustomProperties = {}) -> bytes: ...
