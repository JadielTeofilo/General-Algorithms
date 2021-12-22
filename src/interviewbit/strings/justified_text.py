"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ' ' when necessary so that each line has exactly L characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.


In - words: List[str], line_size: int

What happens when a word is bigger than L
wont be

calculate the size of the words

3 2 6 3 9 8 1 2 3 8
10
3 <5> 2

put first word on result
try to add more, always taking in account a space
need to keep track of the space slots
word(3), space(1), word(2)
count the spaces we have so far, divide the remaining space, and put the mod in the first
Remember to check if its the last line, if its the case, put all spaces to the left


Word

Space

Start

result: List[str]

build_line(words: List[Word], start: Start, size: int) -> str

build_string(result: Union[Word, Space])


"""
import dataclasses
from typing import List, Union, Dict


@dataclasses.dataclass
class Start:
	value: int = 0


@dataclasses.dataclass
class Word:
	value: str = ''
	size: int = 0


@dataclasses.dataclass
class Space:
	size: int = 1


@dataclasses.dataclass
class Line:
	value: List[Union[Word, Space]] = []
	size: int = 0


class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return a list of strings
	def fullJustify(self, words: List[str], line_size: int) -> List[str]:
		start: Start = Start()
		result: List[str] = []
		while start < len(words):
			result.append(
				# Updates the start and builds line
				self.build_line(words, start, line_size)
			)
		return result

	def build_line(words: List[str], start: Start, max_size: int) -> str:
		index: int = start.value
		line: Line = Line([Word(words[index], len(words[index]))], 
						  len(words[index])) 
		index += 1
		while (index < len(words) and 
			   self.fits_next_word(words, index, line, max_size)):  # TODO
			line.value.append(Space(1))
			line.value.append(words[index])
			line.size += len(words[index]) + 1  # adds 1 from space
			index += 1 
		self.rebalance_spaces(line, max_size, words, index)
		start.value = index
		return str(line)  # TODO


	def rebalance_spaces(line: Line, max_size: int, 
						 words: List[str], index: int) -> None:
		spaces_to_add: int = line.size - max_size
		spots_in_line: int = len([token for token in line 
							       if isintance(token, Space)])
		# If no space was inserted (single word line) add 
		# space spot at end
		if not spots_in_line:
			line.append(Space(0))
			spots_in_line = 1
		spaces_per_spot: int = spaces_to_add // spots_in_line
		for token in line:
			if isinstance(token, Space):
				token.size += spaces_per_spot
		remaining_spaces: int = spaces_to_add % spots_in_line
		first_spot: Space = [token for token in line 
							 if isinstance(token, Space)][0]
		first_spot.size += remaining_spaces

