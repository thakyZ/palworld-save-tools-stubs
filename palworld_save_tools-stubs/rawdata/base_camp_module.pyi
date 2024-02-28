from typing import Any, Literal, Sequence

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter

NO_OP_TYPES: list[
    Literal[
        "EPalBaseCampModuleType::Energy",
        "EPalBaseCampModuleType::Medical",
        "EPalBaseCampModuleType::ResourceCollector",
        "EPalBaseCampModuleType::ItemStorages",
        "EPalBaseCampModuleType::FacilityReservation",
        "EPalBaseCampModuleType::ObjectMaintenance",
    ]
]


def decode(
    reader: FArchiveReader, type_name: str, size: int, path: str
) -> dict[str, Any]: ...


def transport_item_character_info_reader(reader: FArchiveReader) -> dict[str, Any]: ...


PASSIVE_EFFECT_ENUM: dict[Literal[0, 1, 2], Literal["EPalBaseCampPassiveEffectType::None", "EPalBaseCampPassiveEffectType::WorkSuitability", "EPalBaseCampPassiveEffectType::WorkHard"]]


def module_passive_effect_reader(reader: FArchiveReader) -> dict[str, Any]: ...


def decode_bytes(
    parent_reader: FArchiveReader, b_bytes: Sequence[int], module_type: str
) -> dict[str, Any]: ...


def encode(
    writer: FArchiveWriter, property_type: str, properties: dict[str, Any]
) -> int: ...


def transport_item_character_info_writer(
    writer: FArchiveWriter, p: dict[str, Any]
) -> None: ...


def module_passive_effect_writer(writer: FArchiveWriter, p: dict[str, Any]) -> None: ...


def encode_bytes(p: dict[str, Any], module_type: str) -> bytes: ...
