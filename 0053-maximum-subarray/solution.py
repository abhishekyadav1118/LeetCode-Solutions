class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize with the first element
        max_so_far = nums[0]
        current_max = nums[0]

        # Iterate through the rest of the array
        for i in range(1, len(nums)):
            # Decide to add the current number to the existing subarray
            # or start a brand new subarray from the current number
            current_max = max(nums[i], current_max + nums[i])

            # Update the global maximum if the current subarray sum is larger
            max_so_far = max(max_so_far, current_max)

        return max_so_far
