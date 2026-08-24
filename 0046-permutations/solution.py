class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(current_path, visited_set):
            # Base case: if the path has all numbers, save it
            if len(current_path) == len(nums):
                result.append(current_path.copy())
                return

            # Explore all possible numbers for the current position
            for num in nums:
                if num not in visited_set:
                    # Choose
                    current_path.append(num)
                    visited_set.add(num)

                    # Explore next positions
                    backtrack(current_path, visited_set)

                    # Unchoose (Backtrack)
                    current_path.pop()
                    visited_set.remove(num)

        backtrack([], set())
        return result
