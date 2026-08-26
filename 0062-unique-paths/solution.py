import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Using the math.comb function for combinations
        return math.comb(m + n - 2, m - 1)
