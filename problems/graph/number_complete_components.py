# Link: https://leetcode.com/problems/count-the-number-of-complete-components/description/

from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors_dict = defaultdict(set)
        for edge in edges:
            u, v = edge
            neighbors_dict[u].add(u)
            neighbors_dict[u].add(v)
            neighbors_dict[v].add(u)
            neighbors_dict[v].add(v)

        counter = 0
        checked = []
        for node in neighbors_dict:
            value = neighbors_dict[node]
            num_neighbors = len(value)
            complete_flag = True
            if value not in checked:
                for neighbor in value:
                    if not (len(neighbors_dict[neighbor]) == num_neighbors and neighbors_dict[neighbor] == value):
                        complete_flag = False
                        break
                if complete_flag:
                    counter += 1
                checked.append(value)

        counter += n - len(neighbors_dict)
        return counter
