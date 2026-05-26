class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max_profit = 0
        for price in prices:
            if price < min:
                min = price
            profit = price - min
            if profit > max_profit:
                max_profit = profit
        return max_profit            
        