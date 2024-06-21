# Link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# The problem guaranteed that a unique solution exists.

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable_vertices = set()
        minimal_vertices = set()
        for edge in edges:
            if edge[1] in minimal_vertices:
                minimal_vertices.remove(edge[1])
            reachable_vertices.add(edge[1])
            if not edge[0] in reachable_vertices:
                minimal_vertices.add(edge[0])
        return list(minimal_vertices)
