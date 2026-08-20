class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Return empty list if input is empty
        if not digits:
            return []

        # Define the phone keypad mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index: int, current_combination: str):
            # Base case: if combination length matches digits length
            if len(current_combination) == len(digits):
                result.append(current_combination)
                return

            # Get letters for current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]

            # Loop through letters and recurse
            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        # Start recursion from index 0
        backtrack(0, "")
        return result
