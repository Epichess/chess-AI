from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar('T')


class Vertex(Generic[T]):
    parent: Vertex
    adjancencyList: list[Vertex]
    value: T

