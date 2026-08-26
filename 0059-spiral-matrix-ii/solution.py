class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Define boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        num = 1
        while num <= n * n:
            # 1. Move right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1  # Shrink top boundary

            # 2. Move down along the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1  # Shrink right boundary

            # 3. Move left along the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1  # Shrink bottom boundary

            # 4. Move up along the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1  # Expand left boundary inward

        return matrix
