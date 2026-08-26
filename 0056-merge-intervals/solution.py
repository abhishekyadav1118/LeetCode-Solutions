class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Handle edge case of an empty input
        if not intervals:
            return []

        # Step 1: Sort intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize merged list with the first interval
        merged = [intervals[0]]

        # Step 3: Iterate and merge
        for current in intervals[1:]:
            last_merged_interval = merged[-1]

            # Overlap check: current start <= last merged end
            if current[0] <= last_merged_interval[1]:
                # Merge by updating the end time
                last_merged_interval[1] = max(last_merged_interval[1], current[1])
            else:
                # No overlap, add the current interval as a new entry
                merged.append(current)

        return merged
