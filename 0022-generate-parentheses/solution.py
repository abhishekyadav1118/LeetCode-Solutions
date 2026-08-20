class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_string, open_count, close_count):
            # Base case: if the string reaches the maximum required length
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            # Rule 1: You can always add an open parenthesis if you haven't used all 'n'
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # Rule 2: You can only add a close parenthesis if it won't exceed open ones
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
