class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the result is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # Array to store the result digits
        res = [0] * (len(num1) + len(num2))

        # Loop from right to left for both numbers
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply digits converted from characters
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))

                # Positions in the result array
                p1 = i + j
                p2 = i + j + 1

                # Add to the current position product sum
                total_sum = mul + res[p2]

                # Update positions with carry handling
                res[p2] = total_sum % 10
                res[p1] += total_sum // 10

        # Convert result array to string, removing leading zero if present
        result_str = []
        for digit in res:
            if not (len(result_str) == 0 and digit == 0):
                result_str.append(str(digit))

        return "".join(result_str)
