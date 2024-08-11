# Link: https://leetcode.com/problems/maximum-total-importance-of-roads/

from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        node_degrees = defaultdict(int)
        for road in roads:
            node_degrees[road[0]] += 1
            node_degrees[road[1]] += 1

        # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        sorted_nodes = sorted(node_degrees, key=node_degrees.get, reverse=True)

        node_value = {}
        for i, node in enumerate(sorted_nodes):
            node_value[node] = n - i

        total_importance = 0
        for road in roads:
            total_importance += node_value[road[0]] + node_value[road[1]]
        return total_importance
