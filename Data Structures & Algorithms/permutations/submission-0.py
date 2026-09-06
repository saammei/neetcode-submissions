class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        picked = [ False ] * len(nums)

        def dfs():
            if len(current) == len(nums):
                res.append(current[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    current.append(nums[i])
                    dfs()
                    current.pop()
                    picked[i] = False
        dfs()
        return res
