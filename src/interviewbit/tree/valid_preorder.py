"""
You are given a preorder traversal A, of a Binary Search Tree.

Find if it is a valid preorder traversal of a BST.



            5
    2                   8
1       3         6           9


5 2 1 3 8 6 9


find the first element to the right that is bigger then the curr root
    while doing so, compare with the max and min values, if invalid, return false
recurse on both sides, sending a max and min element



stops when start == end

return solve(start, mid - 1, max=curr, min=min) and solve(mid, end, max=max, min=curr)
 

Validate if bst has duplicates and where they would fid


In - numbers: List[int]
Out - bool



"""
