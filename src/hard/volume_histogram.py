"""
Volume of Histogram: Imagine a histogram (bar graph). Design an algorithm to compute the
volume of water it could hold if someone poured water across the top. You can assume that each
histogram bar has width 1


Iterate left to right from the first bar
look for a bar bigger than it keeping track of the smaller ones
if found any, calculate the area subtracting by the smaller ones
	continue from that bar
if not found end there

when done, go from right to left, until unvisited nodes adding to total


In - bars: List[int]
Out - volume: int



O(n) where n is the amount of bars
"""
import collections
from typing import List, Iterable, Optional


CalculusResult = collections.namedtuple('CalculusResult', 'value stop')
BarData = collections.namedtuple('BarData', 'value index')


def volume(bars: List[int]) -> int:
	# TODO validate input
	calculus_result: CalculusResult = monotonicly_calculate_volume(
		bars, end=len(bars) - 1
	)
	# Case it went till the end
	if calculus_result.stop == find_last_bar(bars):
		return calculus_result.value
	second_calculus_result: CalculusResult = monotonicly_calculate_volume(
		reversed(bars), 
		# Goes until the last calculated bar
		end=len(bars) - calculus_result.stop - 1
	)
	return second_calculus_result.value + calculus_result.value


def monotonicly_calculate_volume(bars: Iterable[int], 
								 end: int) -> CalculusResult:
	volume: int = 0
	subtracting: int = 0  # For the smaller bars in the middle
	starting_bar: Optional[BarData] = None
	for index, bar in enumerate(bars):
		if index > end:
			break
		if bar == 0:
			continue
		if starting_bar is None:
			starting_bar = BarData(bar, index)
			continue
		if bar >= starting_bar.value:
			volume += ((index - starting_bar.index - 1) *
					   starting_bar.value - subtracting)  
			starting_bar = BarData(bar, index)
			subtracting = 0
		else:
			subtracting += bar
	return CalculusResult(
		volume, 
		starting_bar.index if starting_bar else None
	)


def find_last_bar(bars: List[int]) -> int:
	last_index: int = 0
	for index, bar in enumerate(bars):
		if bar > 0:
			last_index = index
	return last_index


print(
	volume(
		[0,0,4,0,0,6]
	)	
)
