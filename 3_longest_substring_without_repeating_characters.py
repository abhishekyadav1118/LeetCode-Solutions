class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            # Move the left pointer only if the duplicate is inside the current window
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            # Update or insert the current character's last seen position
            char_map[char] = right

            # Calculate current window size and update max_length
            max_length = max(max_length, right - left + 1)

        return max_length