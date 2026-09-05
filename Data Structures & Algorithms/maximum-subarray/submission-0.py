class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        sum_of_array = 0
        for x in nums:
            sum_of_array += x
            res = max(res, sum_of_array)
            if sum_of_array < 0:
                sum_of_array = 0
                continue
        return res
