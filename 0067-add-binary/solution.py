class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Pointers for both strings starting at the last character
        i = len(a) - 1
        j = len(b) - 1

        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            # Append the remainder (0 or 1)
            result.append(str(total % 2))

            # Calculate the new carry (0 or 1)
            carry = total // 2

        # Reverse the result list and join into a string
        return "".join(result[::-1])
