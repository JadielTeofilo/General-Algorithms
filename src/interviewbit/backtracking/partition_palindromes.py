"""
Return all possible palindrome partitioning of s.

For example, given s = "aab",

Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]

    Ordering the results in the answer :

    Entry i will come before Entry j if :

        len(Entryi[0]) < len(Entryj[0]) OR
        (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
        *
        *
        *
        (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))

In the given example,

   ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")


find iterator for mid points
take first midpoint, expand until not a palindrome 
if palindrome does not start at start_index, stop
add to curr and recurse with remaining items
stop when start index >= end


In - word: str
Out - List[List[str]]

"""
import dataclasses
from typing import List, Iterable


@dataclasses.dataclass
class Range:
    # Both non inclusive
    start: int
    end: int


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, word: str) -> List[List[str]]:
        result: List[List[str]] = []
        self.build_partitions(word, start_index=0, 
                            result=result, curr=[])
        result.sort()
        return result

    def build_partitions(self, word: str, start_index: int, 
                         result: List[List[str]], curr: List[str]) -> None:
        if start_index >= len(word):
            result.append(curr)
            return
        for interval in self.find_valid_mid_points(word, start_index):
            self.expand_interval_palindrome(interval, word, start_index) 
            # Stops when curr palindrome does not go all 
            # the way to the left
            if interval.start != start_index - 1:
                continue 
            curr_palindrome: str = word[interval.start+1:interval.end]
            self.build_partitions(word, interval.end, 
                                  result, curr + [curr_palindrome])

    def find_valid_mid_points(self, word: str, start: int) -> Iterable[Range]:
        # efe
        for index in range(start, len(word)):
            yield Range(index - 1, index + 1)
            if index < len(word) - 1:
                yield Range(index, index + 1)

    def expand_interval_palindrome(self, interval: Range, word: str, 
                                   start_index: int) -> None:
        while (interval.start >= start_index and interval.end < len(word) and
               word[interval.start] == word[interval.end]):
            interval.start -= 1
            interval.end += 1 

asdf = Solution()
asdf.partition('efe')
import pdb;pdb.set_trace()
