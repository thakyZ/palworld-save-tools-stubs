from typing import Any, Sequence, Optional

from palworld_save_tools.archive import FArchiveReader, FArchiveWriter

# EPalMapObjectConcreteModelModuleType::None = 0,
# EPalMapObjectConcreteModelModuleType::ItemContainer = 1,
# EPalMapObjectConcreteModelModuleType::CharacterContainer = 2,
# EPalMapObjectConcreteModelModuleType::Workee = 3,
# EPalMapObjectConcreteModelModuleType::Energy = 4,
# EPalMapObjectConcreteModelModuleType::StatusObserver = 5,
# EPalMapObjectConcreteModelModuleType::ItemStack = 6,
# EPalMapObjectConcreteModelModuleType::Switch = 7,
# EPalMapObjectConcreteModelModuleType::PlayerRecord = 8,
# EPalMapObjectConcreteModelModuleType::BaseCampPassiveEffect = 9,
# EPalMapObjectConcreteModelModuleType::PasswordLock = 10,


def module_slot_indexes_reader(reader: FArchiveReader) -> dict[str, Any]: ...


def player_lock_info_reader(reader: FArchiveReader) -> dict[str, Any]: ...


def decode_bytes(
    parent_reader: FArchiveReader, m_bytes: Sequence[int], module_type: str
) -> Optional[dict[str, Any]]: ...


def module_slot_indexes_writer(writer: FArchiveWriter, value: dict[str, Any]) -> None: ...


def player_lock_info_writer(writer: FArchiveWriter, value: dict[str, Any]) -> None: ...


def encode_bytes(p: dict[str, Any], module_type: str) -> bytes: ...
