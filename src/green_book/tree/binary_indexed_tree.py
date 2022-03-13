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

def update(bit: List[int], index: int, value: int) -> None:
    while index < len(bit):
        bit[index] += value
        index += index & -index

def query(bit: List[int], index: int) -> int:
    result: int = 0

