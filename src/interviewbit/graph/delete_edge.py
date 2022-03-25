"""
Given a undirected tree with N nodes labeled  from 1 to N.

Each node has a certain weight assigned to it given by an integer array A of size N.

You need to delete an edge in such a way that Product between sum of weight of nodes in one subtree with sum of weight of nodes in other subtree is maximized.

Return this maximum possible product modulo 109 + 7.



A = [10, 5, 12, 6]
 B = [

        [1, 2]
        [1, 4]
        [4, 3]
     ]

Explanation 1:

 Removing edge (1, 4) created two subtrees.
 Subtree-1 contains nodes (1, 2) and Subtree-2 contains nodes (3, 4)
 So product will be = (A[1] + A[2]) * (A[3] + A[4]) = 15 * 18 = 270

------

The best way to visualise is to think that you are testing splitting the tree into two subtrees, that split will make it so that a given node is going to be a new separete root, and the rest will be the other tree.

Also given its a tree if we know the sum of the whole tree and from all subtrees we just need to go checking against every node.

first find root
    
build Dict[int, List[int]] of relations

for node in inorder():
    curr = ((tree_sum - curr_sum) * curr_sum) % (10**9 + 7)
    max_result = max(max_result, curr)




"""
