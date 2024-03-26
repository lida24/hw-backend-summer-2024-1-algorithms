from typing import TypeVar, Generic

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        stack, visited = [self._root], set()
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
            for neighbour in reversed(vertex.outbound):
                if neighbour not in visited:
                    stack.append(neighbour)
        return result

    def bfs(self) -> list[Node]:
        queue, visited = [self._root], [self._root]
        while queue:
            vertex = queue.pop(0)
            for neighbour in vertex.outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited
