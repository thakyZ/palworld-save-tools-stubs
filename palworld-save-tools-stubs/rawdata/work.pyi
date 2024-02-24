#!/usr/bin/env python3


#pyright: reportMissingTypeStubs=false

from typing import Any, Literal, Sequence

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter

WORK_BASE_TYPES = set[
    Literal[
        # "EPalWorkableType::Illegal",
        "EPalWorkableType::Progress",
        # "EPalWorkableType::CollectItem",
        # "EPalWorkableType::TransportItem",
        "EPalWorkableType::TransportItemInBaseCamp",
        "EPalWorkableType::ReviveCharacter",
        # "EPalWorkableType::CollectResource",
        "EPalWorkableType::LevelObject",
        "EPalWorkableType::Repair",
        "EPalWorkableType::Defense",
        "EPalWorkableType::BootUp",
        "EPalWorkableType::OnlyJoin",
        "EPalWorkableType::OnlyJoinAndWalkAround",
        "EPalWorkableType::RemoveMapObjectEffect",
        "EPalWorkableType::MonsterFarm",
    ]
]


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def decode_bytes(
    parent_reader: FArchiveReader, b_bytes: Sequence[int], work_type: str
) -> dict[str, Any]: ...


def decode_work_assign_bytes(
    parent_reader: FArchiveReader, b_bytes: Sequence[int]
) -> dict[str, Any]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...


def encode_bytes(p: dict[str, Any], work_type: str) -> bytes: ...


def encode_work_assign_bytes(p: dict[str, Any]) -> bytes: ...
