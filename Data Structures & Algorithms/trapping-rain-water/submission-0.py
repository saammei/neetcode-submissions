class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        l_max = height[l]
        r_max = height[r]

        ans = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                if height[l] < l_max:
                    ans += l_max - height[l]
                else:
                    l_max = height[l]
            else:
                r -= 1
                if height[r] < r_max:
                    ans += r_max - height[r]
                else:
                    r_max = height[r]
        return ans
