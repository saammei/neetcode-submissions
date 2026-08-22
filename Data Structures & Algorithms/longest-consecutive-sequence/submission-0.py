class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for x in nums:
            if x - 1 in s:
                continue

            l = 0
            while x in s:
                l += 1
                x += 1
            if l > ans:
                ans = l
        return ans
