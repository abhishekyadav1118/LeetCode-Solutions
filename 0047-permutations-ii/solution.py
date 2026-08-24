from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            # Base case: if the combination is complete
            if len(comb) == len(nums):
                results.append(list(comb))
                return

            # Iterate through unique numbers available
            for num in counter:
                if counter[num] > 0:
                    # Choice
                    comb.append(num)
                    counter[num] -= 1

                    # Explore
                    backtrack(comb, counter)

                    # Undo choice (Backtrack)
                    counter[num] += 1
                    comb.pop()

        # Initialize the frequency map and start backtracking
        backtrack([], Counter(nums))
        return results
