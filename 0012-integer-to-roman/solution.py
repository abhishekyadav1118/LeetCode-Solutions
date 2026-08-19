class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to Roman symbols in descending order (including subtractive forms)
        roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        res = []

        # Loop through the map and greedily deduct values
        for value, symbol in roman_map:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= value * count

        return "".join(res)
