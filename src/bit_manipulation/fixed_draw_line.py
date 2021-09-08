"""
 A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width . Implement a function that draws a horizontal line from (xl, y) to (x2, y).
The method signature should look something like:
drawLine(byte[] screen, int width, int Xl , int x2 , int y)

in - screen: List[int], width: int, x1: int, x2: int, y: int

out - None

How does x1 and x2 works? is it from left to right and indexed at zero?
Yes

by_row = w / 8
start = y * by_row + x1 // 8
end = y * by_row + x2 // 8

O(x1 + x2) time complexity where x1 = x1 and x2 = x2
O(1)


"""
from typing import List


BYTE_LAST_INDEX = 7


def draw_line(screen: List[int], width: int, 
              x1: int, x2: int, y: int) -> None:
    if not screen:
        raise ValueError('Screen with size zero')
    by_row: int = width // 8
    start: int = y * by_row + x1 // 8
    end: int = y * by_row + x2 // 8
    if start == end:
        _update_screen_inside_byte(screen, start, x1 % 8, x2 % 8)
    else:
        _update_screen_inside_byte(screen, start, x1 % 8, BYTE_LAST_INDEX)
        _update_bytes(screen, start=start + 1, end=end - 1)
        _update_screen_inside_byte(screen, end, 0, x2 % 8)
        

def _update_screen_inside_byte(screen: List[int], 
                               byte_index: int, 
                               start: int, end: int) -> None:
    """ Sets 1s on the screen[byte_index] from start to end """
    ones: int = _group_of_ones(size=end - start + 1)
    ones <<= BYTE_LAST_INDEX - end
    screen[byte_index] |= ones


def _group_of_ones(size: int) -> int:
    return (1 << size) - 1


def _update_bytes(screen: List[int], start: int, end: int) -> None:
    """ Sets ones on the screen bytes from start to end """
    for index in range(start, end + 1):
        screen[index] = 0xFF
    
print(draw_line([0xFF], width=8, x1=5, x2=6, y=0))
import pdb;pdb.set_trace()
