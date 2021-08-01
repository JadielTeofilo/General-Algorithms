from typing import List, Iterator, Set
import collections


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V: int, adj: List[List[int]]) -> List[int]:
        """ Returns the sorted array of vertices """
        starting_positions: Iterator[int] = self.find_starting_positions(V, adj)
        visited: Set[int] = set()
        result: List[int] = []
        for starting_position in starting_positions:
            dfs_stack: List[int] = self.build_dfs_stack(adj, starting_position, visited)
            result.extend(dfs_stack)
        return result
        
    def find_starting_positions(self, V: int, adj: List[List[int]]) -> Iterator[int]:
        predecessors: collections.defaultdict = collections.defaultdict(list)
        for src, dst in adj:
            predecessors[dst].append(src)
        for vertex in range(V):
            if not predecessors.get(vertex):
                yield vertex
        
            
    def build_dfs_stack(self, adj: List[List[int]], starting_position: int, visited: Set[int]) -> List[int]:
        """ Fills the dfs stack and returns it """
        if starting_position in visited:
            return []
        stack: List[int] = [starting_position]
        out_stack: List[int] = [starting_position]
        visited.add(starting_position)

        while stack:
            vertex = stack.pop()
            for neighbor in adj[vertex]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                stack.append(neighbor)
                out_stack.append(neighbor)

        return out_stack
