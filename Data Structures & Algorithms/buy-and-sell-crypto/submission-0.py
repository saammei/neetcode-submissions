class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min = prices[0]
        max_profit = 0
        for x in prices:
            if x < last_min:
                last_min = x
            profit = x - last_min
            if max_profit < profit:
                max_profit = profit
        return max_profit
