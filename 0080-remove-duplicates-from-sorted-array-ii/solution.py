class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # 'write' pointer tracks where to insert the next valid element
        write = 2

        # 'read' pointer scans through the array starting from index 2
        for read in range(2, len(nums)):
            # Compare current element with the element two positions behind the write pointer
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
