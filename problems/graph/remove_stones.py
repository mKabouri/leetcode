# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # len(stones) - number_of_cycles
        graph_dict = defaultdict(set)
        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[j][0] == stones[i][0] or stones[j][1] == stones[i][1]:
                    if stones[j] != stones[i]:
                        graph_dict[i].add(j)

        visited = set()
        def dfs(node):
            for neighbor in graph_dict[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        counter = 0
        for i in range(len(stones)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                counter += 1
        return len(stones) - counter
