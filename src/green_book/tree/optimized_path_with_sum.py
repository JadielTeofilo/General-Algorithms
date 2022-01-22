"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative) . Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

In - tree root, target

Out - int amount


If the target is zero, should we return one for the empty sequence?
No


O(N) time complexity
O(d) d is the depth of the tree

"""
from typing import Optional, Dict
import collections
import dataclasses


@dataclasses.dataclass
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def paths_with_sum(root: Node, target: int) -> int:
    """ Finds the amount of paths on the tree 
        that sum up to target """
    running_sums: Dict[int, int] = collections.defaultdict(int)
    result: Dict[str, int] = {'sum': 0}
    paths_with_sum_helper(
        root, target, running_sums, result, current_sum=0
    )
    return result['sum']


def paths_with_sum_helper(node: Node, target: int, 
                          running_sums: Dict[int, int], 
                          result: Dict[str, int], current_sum) -> None:
    """ Updates the result with the amount of paths on 
        the tree that sum up to target """
    if not node:
        return
    current_sum += node.value
    # Updates result according to old running sums
    result['sum'] += running_sums.get(current_sum - target, 0)
    result['sum'] += 1 if target == current_sum else 0
    # Updates old running_sums
    running_sums[current_sum] += 1
    
    paths_with_sum_helper(node.left, target, running_sums,
                          result, current_sum)
    paths_with_sum_helper(node.right, target, running_sums,
                          result, current_sum)
    # Now that node is not on stack, remove its running sum
    running_sums[current_sum] -= 1


import pdb;pdb.set_trace()
