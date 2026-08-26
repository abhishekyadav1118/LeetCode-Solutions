class Solution:
    def isNumber(self, s: str) -> bool:
        # Track state flags
        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True

            elif char in ("+", "-"):
                # Signs can only appear at the start, or immediately after an 'e'/'E'
                if i > 0 and s[i - 1] not in ("e", "E"):
                    return False

            elif char in ("e", "E"):
                # Exponent cannot repeat, and needs a digit before it
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Must be followed by another integer sequence

            elif char == ".":
                # Dot cannot repeat and cannot appear after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True

            else:
                # Any other character is invalid
                return False

        # Must end with a valid digit sequence active
        return seen_digit
