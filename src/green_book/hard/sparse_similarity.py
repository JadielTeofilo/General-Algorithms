"""
Sparse Similarity: The similarity of two documents (each with distinct words) is defined to be the
size of the intersection divided by the size of the union. For example, if the documents consist of
integers, the similarity of {1, 5, 3} and {1, 7, 2, 3} is e. 4, because the intersection has size
2 and the union has size 5.
We have a long list of documents (with distinct values and each with an associated 10) where the
similarity is believed to be "sparse:'That is, any two arbitrarily selected documents are very likely to have similarity O. Design an algorithm that returns a list of pairs of document IDs and the associated similarity.Print only the pairs with similarity greater than o.Empty documents should not be printed at all. For
simplicity, you may assume each document is represented as an array of distinct integers.


The brute force approach is to just go for every document, and for each, compare to all the others

we can use the same idea of the full text search algo and have the numbers point to the keys
then, for each key we can look its numbers and see the documents that are related


Build indexing
iterate on keys building relation tuples
iterate on the relation tuples generating the scores
return output

O(N*K + P*K) time complexity where N is the num of dicts, K is the size of the bigest int list, and P is the number of pairs


In - documents: Dict[int, Set[int]]
Out - List[Pair]

This can be further improved by making find_score use a hash that tells the intersection between pairs

"""
import collections
from typing import Iterable, Set, Dict


Pair = collections.namedtuple('Pair', 'left right')
Result = collections.namedtuple('Result', 'pair value')
Index = Dict[int, Set[int]]


def sparse_similarity(documents: Dict[int, Set[int]]) -> Iterable[Result]:
	index: Index = make_index(documents)
	relations: Iterable[Pair] = build_relations(documents, index)
	for pair in relations:
		score: float = find_score(pair, documents)
		yield Result(pair, score)


def make_index(documents: Dict[int, Set[int]]) -> Index:
	index: Index = collections.defaultdict(set)
	for key, numbers in documents.items():
		for number in numbers:
			index[number].add(key)
	return index


def build_relations(documents: Dict[int, Set[int]], 
					index: Index) -> Iterable[Pair]:
	visited: Set[Pair] = set()
	for key, numbers in documents.items():		
		for number in numbers:
			# Finds all other keys that have that number
			peers: Set[int] = index[number]
			yield from build_pairs(peers, key, visited)


def build_pairs(peers: Set[int], key: int, 
				visited: Set[Pair]) -> Iterable[Pair]:
	for peer in peers:
		if peer == key:
			continue
		# Keeps the smaller key first, so visited can work
		pair: Pair = Pair(left=peer if peer < key else key,
						  right=key if peer < key else peer)
		if pair in visited:
			continue
		visited.add(pair)
		yield pair
	

def find_score(pair: Pair, documents: Dict[int, Set[int]]) -> float:
	return (len(documents[pair.left].intersection(documents[pair.right])) / 
			len(documents[pair.left].union(documents[pair.right])))


print([a for a in sparse_similarity(
documents={
13: {14, 15, 100, 9, 3},
16: {32, 1, 9, 3, 5},
19: {15, 29, 2, 6, 8, 7},
24: {7, 10},
}
)])
