"""
Given a 2D integer matrix A of size N x M.

From A[i][j] you can move to A[i+1][j], if A[i+1][j] > A[i][j], or can move to A[i][j+1] if A[i][j+1] > A[i][j].

The task is to find and output the longest path length if we start from (0, 0).

NOTE:

If there doesn't exist a path return -1.



Since we can only go right and down, we will never loop 
so we can say that dp[row][col] = 1 + max(get_val(dp, row, col+1), get_val(dp, row+1, col))
get val returns 0 if not valid path
iterate backwards on the matrix filling the dp matrix



"""
