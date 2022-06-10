"""
https://leetcode.com/company/google/discuss/2115338/What's-the-solution-or-OA-or-Confidential
Given a Binary String.
Replace all "01" to "10" until it's no more possible. In 1 second you replace all "01" to "10" in next second keep repeating this procedure. Return the total seconds to complete this. eg: 0101->1010->1100 ans:2


0011011
0101101
1010110
1101010
1110100
1111000

dp[i] = dp[i - 1] + i if i - 1 is zero
101101
110110



Explanation:

Example :
String s = "011"
For operation 1 -> 101
For operation 2->110

Output : 2

Example :
String s = "001011";
For operation 1: 010101
For operation 2: 101010
For operation 3: 110100
For operation 4: 111000
Output : 4

Example:
String s = "011010101001010"
Output : 7


ans=0;
int i=n-1;
while(i>=0 && s.charAt(i)=='0'){
      i--;
}

for(;i>=0;i--){
       if(s.charAt(i)=='0'){
                ans=Math.max(ans,ones-1);
                ans++;
                ones=0;
      }
      else{
           ones++; 
     }
}
return ans; ```

What matters here is to mind the group of ones and how they affect the result. We go backwards, counting the size of a given group of ones, when we find a 0 we add one to the answer (but before that we make it be the max(result, ones - 1)) that is because the max group of ones is the one that binds the result.


"""
import unittest


def solve(number: str) -> int:
    result: int = 0
    ones: int = 0
    started: bool = False
    for bit in number[::-1]:
        if not started and bit == '0':
            continue
        started = True
        if bit == '0':
            result = max(ones - 1, result)
            result += 1
            ones = 0
        else:
            ones += 1
    return result


class Test(unittest.TestCase):

    def test_solve(self):
        import pdb;pdb.set_trace()
        
        self.assertEquals(solve('011'), 2)
        self.assertEquals(solve('001011'), 4)
        self.assertEquals(solve('011010101001010'), 7)


unittest.main()
