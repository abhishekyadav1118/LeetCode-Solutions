class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        closest_sum = float("inf")

        # Step 2: Iterate through the array
        for i in range(len(nums) - 2):
            # Step 3: Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Step 5: Update closest sum if a closer one is found
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Step 6: Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Found exact match
                    return current_sum

        return closest_sum
