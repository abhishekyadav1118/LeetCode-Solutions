class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Memoization table to store results of (i, j)
        memo = {}

        def dp(i: int, j: int) -> bool:
            # Check if this state has already been computed
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: If we reach the end of the pattern
            if j == len(p):
                # The string must also be completely matched
                return i == len(s)

            # Check if the current characters match
            # i < len(s) ensures we haven't run out of string characters
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

            # Case 1: The next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                # We have two choices:
                # 1. Skip the '*' and its preceding character (dp(i, j + 2))
                # 2. Use the '*' to match current char, if first_match is true (dp(i + 1, j))
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Case 2: Standard matching moving one character forward
                ans = first_match and dp(i + 1, j + 1)

            # Save to memoization table and return
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
