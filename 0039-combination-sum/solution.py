class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(remain, combo, start):
            # Base case: target reached
            if remain == 0:
                result.append(list(combo))
                return
            # Base case: exceeded target
            elif remain < 0:
                return

            # Explore further combinations
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                # 'i' stays the same to allow reusing the element
                backtrack(remain - candidates[i], combo, i)
                combo.pop()  # Backtrack

        backtrack(target, [], 0)
        return result
