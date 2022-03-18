"""
Problem Description

Given an undirected tree with an even number of nodes. Consider each connection between a parent and child node to be an edge.

You need to remove maximum number of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

Return the maximum number of edges you can remove.



                            1
            4                                   3
    2               9                                   6          
                10        7



 A = 6
 B = [
       [1, 2]
       [1, 3]
       [1, 4]
       [3, 5]
       [4, 6]
     ]

1 3
2 1
3 2
4 2
5 1
6 1
:?

                        1
        2              3                       4       
                        5                       6



maybe have the data on how many nodes each node has bellow it 

if even, then we can just remove that link

Kind of a greedy approach 


fill a Dict[int, List[int]] with the parent child
dfs from root that returns the num of nodes of the tree
has a mutable counter to count removals

O(edges) time 
O(edges) space 
"""
from typing import List, Dict, Optional, Set
import collections


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, size: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        root: int = self.find_root(edges)
        removal: Dict[str, int] = {'count': 0}
        relations: Dict[int, List[int]] = self.build_relations(edges)
        self.find_nodes(root, removal, relations)
        return removal['count']

    def find_root(self, edges: List[List[int]]) -> int:
        parents: Set[int] = set()
        for parent, child in edges:
            parents.discard(child)
            parents.add(parent)
        return parents.pop()
                

    def find_nodes(self, root: int, removal: Dict[str, int], 
                      relations: Dict[int, List[int]]) -> int:
        if root not in relations:
            return 1
        node_count: int = 1
        for relation in relations[root]:
            nodes: int = self.find_nodes(relation, removal, relations)
            if nodes % 2 == 0:
                removal['count'] += 1
            else:
                node_count += nodes
        return node_count

    def build_relations(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        relations: Dict[int, List[int]] = collections.defaultdict(list)
        for parent, child in edges:
            relations[parent].append(child)
        return relations


