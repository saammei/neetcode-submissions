class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            n = (left + right) // 2
            if target == nums[n]:
                return n
            elif target < nums[n]:
                right = n - 1
            else:
                left = n + 1
        return -1