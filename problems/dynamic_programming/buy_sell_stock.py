# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = np.inf
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
