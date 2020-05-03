class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dictionary for letter used in the current string
        letters = {}
        current_longest = 0
        index = 0
        for i, c in enumerate(s):
            if c in letters:
                current_longest = max(current_longest, i-index)
                index = max(index, letters[c] + 1)  # slide the window forward from the left
            letters[c] = i
        return max(current_longest, len(s)-index)
