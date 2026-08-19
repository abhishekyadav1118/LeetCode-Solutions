class Solution:

    def romanToInt(self, s: str) -> int:
        # Step 1: Map symbols to their integer values
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        n = len(s)

        # Step 2: Iterate through the string
        for i in range(n):
            # Check if current value is less than the next value
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]  # Subtraction rule
            else:
                total += roman_map[s[i]]  # Addition rule

        return total
