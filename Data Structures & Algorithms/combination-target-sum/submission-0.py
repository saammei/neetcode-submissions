class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []

        def backtrack(i, total):
            if total == target:
                res.append(subset[:])
                return
            if total > target or i >= len(nums):
                return
            subset.append(nums[i])
            backtrack(i, total + nums[i])
            subset.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res
