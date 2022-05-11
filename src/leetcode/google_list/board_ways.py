"""
In how many ways you can build a tower of height n, using 1X3, 2X3, and 3X3 blocks.
[ ][ ][ ]
[ ][ ][ ] [ ][ ][ ]
[ ][ ][ ] [ ][ ][ ] [ ][ ][ ]

You can use any number of blocks, and rotations are counted as different.

Examples:

    n=1 : only way we can build a tower of height 1 and width 3 is by picking 1 1X3 matrix.

    n=2 : 2 ways, i.e chose 2 blocks of 1X3 or 1 block of 2X3.

    rotation don't really count as they'd be the same orientaion in the above base cases.

    n=3 : 6 ways

Let's say 000 -1X3's and xxx represents 2X3's and Y's represents 3X3 so we have following ways:

                        vertical 0s
000 XXX 000 0XX XX0 YYY 000
000 XXX XXX 0XX XX0 YYY 000
000 000 XXX 0XX XX0 YYY 000

Interviewer helped me to find the combinations for n=3 in interview I counted 7, and he agreed :|, which if I think now is wrong since the case below wouldn't be valid:
XXX
000
XXX


n = 4

since we only care about the height and the number of ways, we can think of this problem like the decode ways

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 7

dp[i] =
    dp[i - 1] when last block has height 1
    2 * dp[i - 2] when last block has height 2 (there are two ways of doing it)
    3 * dp[i - 3] when last block has hiehgt 3 (there are three ways of doing it (excluding 3 1x3s cuz its covered by above cases))

"""
