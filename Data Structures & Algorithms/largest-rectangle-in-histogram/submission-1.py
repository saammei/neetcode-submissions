class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, h in enumerate(heights):
            left = right = i
            while left > -1 and heights[left] >= h:
                left -= 1
            while right < len(heights) and heights[right] >= h:
                right += 1

            print(i, h, left, right)
            area = (right - left - 1) * h
            max_area = max(area, max_area)
        return max_area
