# pyright: reportArgumentType=false
# pylint: disable=C0114,C0301

from typing import Any, Callable, Literal

PalworldTypeHints = dict[
    Literal[
        ".worldSaveData.CharacterContainerSaveData.Key",
        ".worldSaveData.CharacterSaveParameterMap.Key",
        ".worldSaveData.CharacterSaveParameterMap.Value",
        ".worldSaveData.FoliageGridSaveDataMap.Key",
        ".worldSaveData.FoliageGridSaveDataMap.Value.ModelMap.Value",
        ".worldSaveData.FoliageGridSaveDataMap.Value.ModelMap.Value.InstanceDataMap.Key",
        ".worldSaveData.FoliageGridSaveDataMap.Value.ModelMap.Value.InstanceDataMap.Value",
        ".worldSaveData.FoliageGridSaveDataMap.Value",
        ".worldSaveData.ItemContainerSaveData.Key",
        ".worldSaveData.MapObjectSaveData.MapObjectSaveData.ConcreteModel.ModuleMap.Value",
        ".worldSaveData.MapObjectSaveData.MapObjectSaveData.Model.EffectMap.Value",
        ".worldSaveData.MapObjectSpawnerInStageSaveData.Key",
        ".worldSaveData.MapObjectSpawnerInStageSaveData.Value",
        ".worldSaveData.MapObjectSpawnerInStageSaveData.Value.SpawnerDataMapByLevelObjectInstanceId.Key",
        ".worldSaveData.MapObjectSpawnerInStageSaveData.Value.SpawnerDataMapByLevelObjectInstanceId.Value",
        ".worldSaveData.MapObjectSpawnerInStageSaveData.Value.SpawnerDataMapByLevelObjectInstanceId.Value.ItemMap.Value",
        ".worldSaveData.WorkSaveData.WorkSaveData.WorkAssignMap.Value",
        ".worldSaveData.BaseCampSaveData.Key",
        ".worldSaveData.BaseCampSaveData.Value",
        ".worldSaveData.BaseCampSaveData.Value.ModuleMap.Value",
        ".worldSaveData.ItemContainerSaveData.Value",
        ".worldSaveData.CharacterContainerSaveData.Value",
        ".worldSaveData.GroupSaveDataMap.Key",
        ".worldSaveData.GroupSaveDataMap.Value",
        ".worldSaveData.EnemyCampSaveData.EnemyCampStatusMap.Value",
        ".worldSaveData.DungeonSaveData.DungeonSaveData.MapObjectSaveData.MapObjectSaveData.Model.EffectMap.Value",
        ".worldSaveData.DungeonSaveData.DungeonSaveData.MapObjectSaveData.MapObjectSaveData.ConcreteModel.ModuleMap.Value",
    ],
    Literal[
        "StructProperty",
        "Guid",
    ],
]

PalworldCustomProperties = dict[
    Literal[
        ".worldSaveData.GroupSaveDataMap",
        ".worldSaveData.CharacterSaveParameterMap.Value.RawData",
        ".worldSaveData.ItemContainerSaveData.Value.RawData",
        ".worldSaveData.ItemContainerSaveData.Value.Slots.Slots.RawData",
        ".worldSaveData.CharacterContainerSaveData.Value.Slots.Slots.RawData",
        ".worldSaveData.DynamicItemSaveData.DynamicItemSaveData.RawData",
        ".worldSaveData.FoliageGridSaveDataMap.Value.ModelMap.Value.RawData",
        ".worldSaveData.FoliageGridSaveDataMap.Value.ModelMap.Value.InstanceDataMap.Value.RawData",
        ".worldSaveData.BaseCampSaveData.Value.RawData",
        ".worldSaveData.BaseCampSaveData.Value.WorkerDirector.RawData",
        ".worldSaveData.BaseCampSaveData.Value.WorkCollection.RawData",
        ".worldSaveData.BaseCampSaveData.Value.ModuleMap",
        ".worldSaveData.WorkSaveData",
        ".worldSaveData.MapObjectSaveData",
    ],
    tuple[
        Callable[[FArchiveReader, str, int, str], dict[str, Any]],
        Callable[[FArchiveWriter, str, dict[str, Any]], int],
    ],
]