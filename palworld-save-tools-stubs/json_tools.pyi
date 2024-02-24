#!/usr/bin/env python3


#pyright: reportIncompatibleMethodOverride=false, reportMissingTypeStubs=false

import json
import uuid
from typing import Any

from palworld_save_tools.archive import UUID


class CustomEncoder(json.JSONEncoder):
    def default(self, obj: UUID | uuid.UUID | Any) -> str: ...
