"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.




                    1

                    2

                    3 6 6 6 6

                    4

                    5



we could for every node try to keep track of the two furthest element away from it for every edge it has

distance: int 
path_first_node: int


Key is to know that you are finding the middle elements and there are only two of them

another approach is to think of a topological sort (for undirected graphs) where we sort by number of edges trimming the leafs

the idea is to use bfs

add all nodes with only one neighbor 

pop from queue, go on its neighbors removing it from its edges, if one of them ends up with one edge, add to the queue

stop when only two elements are on the queue

check if they have the same distance, if so return both, else return the bigger distance


O(n) time complexity where n is the num of nodes
O(n) space complexity cuz the queue will not have a given node more then once

"""
import collections
from typing import Dict, Set, Deque, List


Graph = Dict[int, Set[int]]
QueueValue = collections.namedtuple('QueueValue', 'key distance')


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [0]
        graph: Graph = build_graph(edges)
        queue: Deque[QueueValue] = build_queue(graph)
        find_mid_nodes(queue, graph)
        if len(queue) == 1:
            return queue[0].key
        if queue[0].distance != queue[1].distance:
            return (queue[0].key 
                    if queue[0].distance > queue[1].distance 
                    else queue[1].key)
        return [item.key for item in queue]


def find_mid_nodes(queue: Deque[QueueValue], graph: Graph) -> None:
    while len(graph) > 2 and queue:
        key, distance = queue.popleft()
        neighbor: int = graph.pop(key)
        graph[neighbor].remove(key)
        if len(graph[neighbor]) == 1:
            queue.append(QueueValue(neighbor, distance + 1))


def build_graph(edges: List[List[int]]) -> Graph:
    graph: Graph = collections.defaultdict(set)
    for start, end in edges:
        graph[start].add(end)
        graph[end].add(start)
    return graph


def build_queue(graph: Graph) -> Deque[QueueValue]:
    queue: Deque[QueueValue] = collections.deque()
    for key in graph:
        if len(graph[key]) == 1:
            queue.append(QueueValue(key, 0))
    return queue





