class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            total_time = sum((x + mid - 1)//mid for x in piles)
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return left
