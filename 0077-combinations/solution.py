class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start: int, current_combination: list[int]):
            # If the combination reaches the required length, save it
            if len(current_combination) == k:
                result.append(list(current_combination))
                return

            # Optimization: No need to loop if there aren't enough numbers left to fill k
            for i in range(start, n - (k - len(current_combination)) + 2):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Undo choice (backtrack)

        backtrack(1, [])
        return result
