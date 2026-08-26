class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        last_index = len(nums) - 1

        for i, jump in enumerate(nums):
            # If current index is unreachable, stop
            if i > max_reach:
                return False

            # Update the maximum reachable index
            max_reach = max(max_reach, i + jump)

            # Optimization: Early exit if last index is reached
            if max_reach >= last_index:
                return True

        return max_reach >= last_index
