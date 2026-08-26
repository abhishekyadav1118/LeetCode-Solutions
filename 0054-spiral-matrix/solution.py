class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        # Initialize the four boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # 1. Traverse from left to right across the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down

            # 2. Traverse from top to bottom down the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary left

            # CRITICAL CHECK: Check if boundaries crossed after updating top/right
            if not (left <= right and top <= bottom):
                break

            # 3. Traverse from right to left across the bottom row
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1  # Move the bottom boundary up

            # 4. Traverse from bottom to top up the left column
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1  # Move the left boundary right

        return result
