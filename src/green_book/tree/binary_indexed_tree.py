"""
Implementation of BIT

It is a kind of segment tree. A tree that keeps that each node keeps the agreggate of a range

root keeps the aggregate of the whole list, left, from the first half, right, from the second half

the goal is to be able to update data in log n and find data (exact and closest) in log n

The bit does it with an array
              {           a[x],                  if x is odd
BIT[x] =                    a[1] + ... + a[x],     if x is power of 2
                            a[last pow]+...+a[x] if even but not power of 2
               }



"""


class BIT:

    def __init__(self, size) -> None:
        self.tree: List[int] = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index  # Givest the last set bit

    def query(self, index: int) -> int:
        result: int = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


