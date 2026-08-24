class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # Sort to easily skip duplicate elements
        candidates.sort()
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If current candidate exceeds target, no point continuing the loop
                if candidates[i] > target:
                    break
                    
                # Skip duplicate elements to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                path.append(candidates[i])
                # i + 1 because each number can only be used once
                backtrack(i + 1, target - candidates[i], path)
                path.pop() # Backtrack
                
        backtrack(0, target, [])
        return res