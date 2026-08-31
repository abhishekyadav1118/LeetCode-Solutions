class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Initialize the first two steps
        first = 1
        second = 2

        # Iteratively calculate ways for subsequent steps
        for _ in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second
