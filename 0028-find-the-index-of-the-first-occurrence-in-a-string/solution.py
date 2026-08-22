class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, return 0 (standard behavior)
        if not needle:
            return 0

        h_len, n_len = len(haystack), len(needle)

        # Only iterate up to where the needle can still fit
        for i in range(h_len - n_len + 1):
            # Check if the substring matches the needle
            if haystack[i : i + n_len] == needle:
                return i

        return -1
