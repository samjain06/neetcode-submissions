"""
input = 3
output = 3
number of ways = 1 + 1 + 1, 1+2, 2+1

                 root
                   3
           (n-2)/    \\ (n-1)
               1      2
              / \\   / \\
            -1   1  0   1
                       / \\
                     -1   0

total three ways we can reach 0
PSEDUCODE:

def climb_stairs(n):
    result = 0

    def helper(n):
        base case would be to return 0 if n is 1 else False

        recursive case
        this would be to add the result of when we take 1 step and 2 steps

    call helper with n
    return result
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        num_of_ways = 0
        memo = {}

        def helper(n):
            # base case
            if n == 0:
                return 1
            elif n < 0:
                return 0

            # recursive case
            if n in memo:
                return memo[n]

            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

        num_of_ways = helper(n)
        return num_of_ways
