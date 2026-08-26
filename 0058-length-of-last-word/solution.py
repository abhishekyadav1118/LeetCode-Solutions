class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without arguments automatically removes trailing spaces
        # and splits the string by any consecutive whitespace.
        words = s.split()

        # Return the length of the last word in the list.
        return len(words[-1])
