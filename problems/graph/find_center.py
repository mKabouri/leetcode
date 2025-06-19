# Link: https://leetcode.com/problems/find-center-of-star-graph/description

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for u, v in edges:
            if u in visited:
                return u
            if v in visited:
                return v
            visited.add(u)
            visited.add(v)
