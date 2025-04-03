# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            profit = prices[i+1] - prices[i]
            if profit > 0:
                total_profit += profit
        return total_profit


s = Solution()
assert s.maxProfit([7,1,5,3,6,4]) == 7
assert s.maxProfit([1,2,3,4,5]) == 4
assert s.maxProfit([7,6,4,3,1]) == 0
print("PASS", __file__)