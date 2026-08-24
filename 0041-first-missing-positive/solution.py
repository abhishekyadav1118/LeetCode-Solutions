class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Cycle sort / place each number at its correct index
        for i in range(n):
            # Keep swapping until the element at i is in the correct place
            # or it is out of the valid range [1, n]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Look for the first mismatch
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers 1 to n are present
        return n + 1
