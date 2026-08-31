class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0

        for w in words:
            # Check if adding the next word exceeds maxWidth
            # len(cur) represents the minimum number of spaces needed between words
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces for the current complete line
                for i in range(maxWidth - num_of_letters):
                    # Loop through the gaps between words dynamically
                    # If it's a single-word line, pad spaces at the end (index 0)
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur, num_of_letters = [], 0

            cur.append(w)
            num_of_letters += len(w)

        # Format the last line: left-justified with trailing spaces
        last_line = " ".join(cur)
        trailing_spaces = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_spaces)

        return res
