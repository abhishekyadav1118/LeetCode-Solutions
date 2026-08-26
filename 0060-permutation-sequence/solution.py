import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers: [1, 2, 3, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]

        # Convert k to 0-indexed
        k -= 1

        result = []

        # Determine each position from left to right
        for i in range(n, 0, -1):
            # Number of permutations per block for the remaining elements
            block_size = math.factorial(i - 1)

            # Find the index of the number to pick
            index = k // block_size

            # Append the selected number and remove it from our available pool
            result.append(numbers.pop(index))

            # Update k for the next position
            k %= block_size

        return "".join(result)
