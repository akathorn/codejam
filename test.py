import sys
from functools import lru_cache
from typing import Any, Callable, List, NamedTuple, Tuple, TypeVar, Union


Module = NamedTuple("Module", [("id", int), ("fun", int), ("pointers", list)])


@lru_cache()
def cached(modules: Tuple[Module]):
    print("caching...")
    return 0


cached((Module(id=0, fun=0, pointers=[])))