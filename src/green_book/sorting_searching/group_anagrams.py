"""
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.

In - words: List[str]
Out - List[str]

anagrams are permutations that are on the dictionary 
if you compare two anagrams on sorted order they are the same

if we create a tupple (sorted_anagram, anagram) and sort them all we would have the desired order

O(K*nlog(n)) to sort each anagram where n is the size of the bigger anagram and K the amount of words

O(n*Klog(K)) to sort the whole list

O(K*n*(nlog(n) + Klog(K))) time complexity
O(K*n) space complexity

If instead of sorting grouping is used:

O(K*nlog(n))


"""
from typing import List, Dict
import collections


Words = Dict[str, List[str]]


def group_anagrams(words: List[str]) -> List[str]:
	word_groups: Words = collections.defaultdict(list)
	for word in words:
		word_groups[''.join(sorted(word))].append(word)
	result: List[str] = []
	for words in word_groups.values():	
		result.extend(words)
	return result


asdf = ['fdsa', 'sdfa', 'aba', 'rewq', 'baa', 'qwer', 'asdf']
print(asdf)
print(group_anagrams(asdf))
import pdb;pdb.set_trace()
