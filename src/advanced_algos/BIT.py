"""

Binary indexed Tree

"""


class BIT:

    def __init__(self, size: int) -> None:
        self._tree: List[int] = [0] * (size + 1)

    def query(self, index: int) -> int:
        result: int = 0
        while index > 0:
            result += self._tree[index]
            index -= index & -index
        return result

    def insert(self, index: int, value: int) -> None:
        while index < len(self._tree):
            self._tree[index] += value
            index += index & -index





