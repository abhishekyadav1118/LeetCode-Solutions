class Solution:

    def jump(self, nums: list[int]) -> int:
        # If the array has 1 element, we are already at the end.
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # We don't need to process the last element because once we reach
        # or surpass the last index, we stop.
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current index
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of the current jump's range
            if i == current_end:
                jumps += 1  # We must take another jump
                current_end = farthest  # Update the range for the next jump

                # Optimization: If the current range already reaches the end, stop early
                if current_end >= len(nums) - 1:
                    break

        return jumps
