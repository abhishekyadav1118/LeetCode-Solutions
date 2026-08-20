class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their matching opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else "#"

                # If the mapping doesn't match the top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
