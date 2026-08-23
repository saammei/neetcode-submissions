class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_to_index = {}
        for i, ch in enumerate(s):
            if ch in char_to_index and char_to_index[ch] >= left:
                left = char_to_index[ch] + 1
            char_to_index[ch] = i
            max_length = max(max_length, i - left + 1)
        return max_length
