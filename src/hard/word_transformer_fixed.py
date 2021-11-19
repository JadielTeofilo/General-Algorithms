"""
Word Transformer: Given two words of equal length that are in a dictionary, write a method to
transform one word into another word by changing only one letter at a time. The new word you get
in each step must be in the dictionary.

It is possible to group all the words with one edit distance away by generating a generic term
like the following: aba = _ba, a_a, ab_


From there you have a graph problem, to find a path. 

Bidirectional search can be used with bfs
use a queue

In - origin: str, target: str, dictionary: List[str]
Out - List[str]

"""
import collections
from typing import List, Dict, Set, Iterable


Graph = Dict[str, Set[str]]
Queue = collections.deque
PathData = collections.namedtuple('PathData', 'word path')


def word_transformer(origin: str, target: str, 
                     dictionary: List[str]) -> List[str]:
    # TODO Validate the input
    graph: Graph = build_graph(dictionary) 
    return bidirectional_search(origin, target, graph)


def build_graph(dictionary: List[str]) -> Graph:
    graph: Graph = collections.defaultdict(set)
    for word in dictionary:
        for variation in get_generic_variations(word):
            graph[variation].add(word)
    return graph


def bidirectional_search(origin: str, target: str, 
                         graph: Graph) -> List[str]:
    origin_queue: Queue = collections.deque([PathData(origin, [])])
    target_queue: Queue = collections.deque([PathData(target, [])])
    origin_visited: Dict[str, PathData] = {}
    target_visited: Dict[str, PathData] = {}
    while origin_queue and target_queue:
        path: List[str] = find_path(origin_queue, origin_visited, 
                                    target_visited, graph)
        if not path:
            path = find_path(target_queue, target_visited, 
                             origin_visited, graph)
            path.reverse()
        if path:
            return path
    return []


def find_path(queue: Queue, visited: Dict[str, PathData], 
              other_visited: Dict[str, PathData], graph: Graph) -> List[str]:

    node: PathData = queue.popleft()
    if node.word in visited:
        return []
    visited[node.word] = node
    # Looks to see if other leg of bfs toutched it
    if node.word in other_visited:
        # reverses the other side of the path bfs
        other_visited_path = [node for node in 
                              reversed(other_visited[node.word].path)]
        # Concatenates both sides of the path
        return node.path + [node.word] + other_visited_path
    for generic_word in get_generic_variations(node.word):
        for neighbor in graph.get(generic_word, []):
            if neighbor == node.word:
                continue
            queue.append(PathData(neighbor, node.path + [node.word]))
    return []


def get_generic_variations(word: str) -> Iterable[str]:
    for i in range(len(word)):
        yield word[:i] + '_' + word[i+1:]


print(
    word_transformer(
        'damp', 'like', ['damp', 'lamp', 'dump', 'dimp', 'divp', 'dive', 'lime', 'dime', 'like', 'limp']
    )
)

