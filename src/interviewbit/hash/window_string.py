"""

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.

Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :

ADOBECODEB A  N  C
0123456789 10 11 12
T = "ABC"

match_size  # To be able to tell when we matched all letters
match_count = Counter
start_order: deque = [
('C', 5),
(B, 9)
(A, 10)

]
min_size: int  # min size
position: Position
target_count Counter



no match, countinue
when found a match, add to the queue, add to the counter
if counter of char not more then target, add to match size

    updating the counter

if word is fully matched update result when needed

Minimum window is "BANC"

    Note:

        If there is no such window in S that covers all characters in T, return the empty string ''.
        If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).

In - text: str, word: str
Out - str

"""
from typing import Set
import collections
import dataclasses


@dataclasses.dataclass
class Position:
    start: int
    end: int


CharData = collections.namedtuple('CharData', 'index char')


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, text: str, word: str) -> str:
        if not word:
            return word
        match_size = 0  # To be able to tell when we matched all letters
        match_count: collections.Counter = collections.Counter()
        target_count: collections.Counter = collections.Counter(word)
        start_order = collections.deque()
        min_size: int = len(text) + 1  # Starts at 'infinite'
        position: Position = Position(0, 0)
        cache: Set[str] = set(word)
        for index, char in enumerate(text):
            if char not in cache:
                continue
            start_order.append(CharData(index, char))
            match_count[char] += 1
            if match_count[char] <= target_count[char]:
                match_size += 1
            self.zip_queue(start_order, match_count, target_count)
            if (match_size >= len(word) and 
                min_size > self.get_curr_size(index, start_order)):
                self.update_position(index, start_order, position)
                min_size = self.get_curr_size(index, start_order)
        return text[position.start:position.end + 1]

    def zip_queue(self, start_order: collections.deque, 
                  match_count: collections.Counter, 
                  target_count: collections.Counter) -> None:
        """
        Updates start_order check if the top of queue 
        has more elements than it needs, pop until not needed
        """
        while self.has_more_then_needs(
            start_order, match_count, target_count
        ):
            char_data: CharData = start_order.popleft()
            match_count[char_data.char] -= 1

    def has_more_then_needs(
        self, start_order: collections.deque, 
        match_count: collections.Counter, 
        target_count: collections.Counter
    ) -> bool:
        char_data: CharData = start_order[0]
        return match_count[char_data.char] > target_count[char_data.char]

    def get_curr_size(self, index: int, start_order: collections.deque) -> int:
        return index - start_order[0].index + 1

    def update_position(self, index: int, 
                        start_order: collections.deque, 
                        position: Position) -> None:
        position.start = start_order[0].index
        position.end = index
        

