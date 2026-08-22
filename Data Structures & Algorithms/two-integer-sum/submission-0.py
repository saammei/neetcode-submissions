class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in stored:
                return [stored[y], i]
            stored[x] = i
        return []