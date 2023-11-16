from typing import TypeVar


T = TypeVar('T')


def flatten_array(items: list[list[T]]) -> list[T]:
    base: list[T] = []
    for item in items:
        base = base + item
    return base
