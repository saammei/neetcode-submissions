class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        left = 0
        max_freq = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in char_freq:
                char_freq[ch] += 1
            else:
                char_freq[ch] = 1
            max_freq = max(max_freq, char_freq[ch])
            while (i - left + 1) - max_freq > k:
                char_freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len
