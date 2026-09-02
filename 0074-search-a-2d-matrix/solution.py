class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize binary search boundaries on the virtual 1D array
        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2

            # Map the 1D index back to 2D coordinates
            row = mid // cols
            col = mid % cols

            # Get the value at the middle position
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
