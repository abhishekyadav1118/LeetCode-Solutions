class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the current water volume
            current_width = right - left
            current_height = min(height[left], height[right])
            current_water = current_width * current_height

            # Update maximum water found
            max_water = max(max_water, current_water)

            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
