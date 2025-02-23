# Link: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

from math import ceil
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount)/2))
