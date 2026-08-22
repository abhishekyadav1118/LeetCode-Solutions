from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result = []

        # Run a sliding window starting at each possible offset
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0

            # Slide the window across the string
            while right + word_len <= len(s):
                # Get the next word from the right side of the window
                word = s[right : right + word_len]
                right += word_len

                if word in word_counts:
                    current_counts[word] += 1
                    count += 1

                    # If a word occurs more times than required, shrink from the left
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If all words match perfectly, record the starting index
                    if count == num_words:
                        result.append(left)

                else:
                    # Invalid word encountered: reset the current window completely
                    current_counts.clear()
                    count = 0
                    left = right

        return result
