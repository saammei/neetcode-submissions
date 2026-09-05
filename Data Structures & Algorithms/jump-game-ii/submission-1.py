class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        farthest = 0
        cur_jump_end = 0
        for i, x in enumerate(nums):
            farthest = max(farthest, x + i)
            if i == cur_jump_end:
                jumps += 1
                cur_jump_end = farthest
                if cur_jump_end >= len(nums) - 1:
                    break
        return jumps

