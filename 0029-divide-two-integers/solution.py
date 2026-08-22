class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the quotient
        # True if result is negative, False if positive
        is_negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        # Perform division using bit shifting
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1

            # Shift left until temp_divisor * 2 exceeds abs_dividend
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the largest found multiple from dividend
            abs_dividend -= temp_divisor
            quotient += multiple

        # Apply the sign to the final result
        if is_negative:
            quotient = -quotient

        # Clamp the result within 32-bit integer bounds
        return max(INT_MIN, min(INT_MAX, quotient))
