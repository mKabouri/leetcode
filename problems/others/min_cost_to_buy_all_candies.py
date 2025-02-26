# Link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        min_cost = 0
        n = len(cost)
        i = 0
        while i < n:
            if i + 1 >= n:
                min_cost += cost[i]
            else:
                min_cost += cost[i] + cost[i+1]
            i += 3
        return min_cost
