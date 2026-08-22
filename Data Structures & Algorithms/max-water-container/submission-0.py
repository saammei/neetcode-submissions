class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            h = min(heights[left], heights[right])
            x = (right - left) * h
            if x > ans:
                ans = x
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans
