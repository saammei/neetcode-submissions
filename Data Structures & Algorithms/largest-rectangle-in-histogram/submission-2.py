class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
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
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid_index = stack.pop()
                left = stack[-1]
                right = i
                w = right - left - 1
                max_area = max(max_area, heights[mid_index] * w)
            stack.append(i)
        return max_area
