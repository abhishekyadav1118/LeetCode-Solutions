class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # Append a copy of the current subset to the result
            res.append(list(path))

            # Explore further elements to build larger subsets
            for i in range(start, len(nums)):
                path.append(nums[i])  # Make a choice
                backtrack(i + 1, path)  # Move to the next element
                path.pop()  # Undo the choice (backtrack)

        backtrack(0, [])
        return res
