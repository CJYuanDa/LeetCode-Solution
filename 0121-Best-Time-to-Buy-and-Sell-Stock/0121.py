from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        temp_profit = 0
        profit = 0

        for i in range(len(prices)):
            if i == 0:
                buy = prices[i]
                continue
            
            if prices[i] < buy:
                buy = prices[i]

            if prices[i] > buy:
                temp_profit = prices[i] - buy

            if temp_profit > profit:
                profit = temp_profit
            
            temp_profit = 0
            
        return profit