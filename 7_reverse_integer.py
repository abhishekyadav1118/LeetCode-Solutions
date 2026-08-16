class Solution:

    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -(2**31), 2**31 - 1

        # Track the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            # Extract the last digit
            digit = x % 10
            x //= 10

            # Append the digit to the reversed number
            reversed_num = reversed_num * 10 + digit

        # Apply the original sign
        reversed_num *= sign

        # Check for 32-bit overflow
        if reversed_num < MIN_INT or reversed_num > MAX_INT:
            return 0

        return reversed_num