class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps: List[int] = get_lps(needle)
        needle_index: int = 0
        if not needle:
            return 0
        for index, char in enumerate(haystack):
           while needle_index > 0 and needle[needle_index] != char:
                needle_index = lps[needle_index - 1]

            if needle[needle_index] == char:
                needle_index += 1
            if needle_index == len(needle):
                return index - len(needle) + 1
        return -1
    
def get_lps(needle: str) -> List[int]:
    lps: List[int] = [0] * len(needle)
    prefix_size: int = 0
    
    for index, char, in enumerate(needle):
        while prefix_size > 0 and needle[prefix_size] != char:
            prefix_size = lps[prefix_size - 1]
        if needle[prefix_size] == char and index != 0:
            prefix_size += 1
            lps[index] = prefix_size
    return lps
