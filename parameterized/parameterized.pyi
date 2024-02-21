#!/usr/bin/env python3

from typing import Callable, Any, Iterable

class parameterized(object):
    @classmethod
    def expand(cls, input: Iterable[Any], name_func: Callable[..., str] | None = None,
               doc_func: Callable[..., str] | None = None, skip_on_empty: bool = False,
               namespace: dict[str, Any] | None = None, **legacy: Any) -> Any: ...
