"""
Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

    You must change exactly one character in every transformation.
    Each intermediate word must exist in the dictionary.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.

Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.

Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3

Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

build the edges between the words:
    _ot: hot, dot, lot
    h_t: hot
     and so on
    Iterate on the list of words + start and target to do that
    for each word generate the n variations (n = size of word)

then just do a bfs from the start until we reach target


Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"


"""
