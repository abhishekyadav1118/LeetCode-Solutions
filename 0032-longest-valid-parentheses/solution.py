class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for length calculation
        max_len = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Stack is empty; push current index as new base
                    stack.append(i)
                else:
                    # Stack is not empty; calculate valid length
                    max_len = max(max_len, i - stack[-1])

        return max_len
