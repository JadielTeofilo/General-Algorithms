Count = collections.namedtuple('Count', 'zeros ones')


class Solution:
    def numberOfWays(self, word: str) -> int:
        """
        Input: s = "001101"
        Output: 6
        Explanation: 
        The following sets of indices selected are valid:
        - [0,2,4] from "001101" forms "010"
        - [0,3,4] from "001101" forms "010"
        - [1,2,4] from "001101" forms "010"
        - [1,3,4] from "001101" forms "010"
        - [2,4,5] from "001101" forms "101"
        - [3,4,5] from "001101" forms "101"
        
        Since its only Three, think of the possible buildings
        
        The idea is to find num of subsequences like 101 or 010
        Pattern tidy triplet, take the mid element:
            if zero the num of ways that it will make the triplet is ones_on_left * ones_on_right
            if 1 the num of ways that it will make the triplet is zeros_on_left * zeros_on_right
        
        """
        prefix: List[Count] = self.build_prefix(word)
        suffix: List[Count] = self.build_suffix(word)
        result: int = 0
        for i in range(1, len(word) - 1):
            char: str = word[i]
            if char == '0':
                result += prefix[i - 1].ones * suffix[i + 1].ones
            else:
                result += prefix[i - 1].zeros * suffix[i + 1].zeros
        return result
            
    def build_prefix(self, word: str) -> List[Count]:
        if not word:
            return []
        prefix: List[Count] = [0] * len(word)
        prefix[0] = Count(zeros=int(word[0] == '0'), ones=int(word[0] == '1'))
        for i in range(1, len(word)):
            prefix[i] = Count(zeros=prefix[i - 1].zeros + int(word[i] == '0'), 
                              ones=prefix[i - 1].ones + int(word[i] == '1'))
        return prefix
            
    def build_suffix(self, word: str) -> List[Count]:
        if not word:
            return []
        suffix: List[Count] = [0] * len(word)
        suffix[-1] = Count(zeros=int(word[-1] == '0'), ones=int(word[-1] == '1'))
        for i in range(len(word) -2, -1, -1):
            suffix[i] = Count(zeros=suffix[i + 1].zeros + int(word[i] == '0'), 
                              ones=suffix[i + 1].ones + int(word[i] == '1'))
        return suffix
    
        
