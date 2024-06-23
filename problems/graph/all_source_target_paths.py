# Link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        destination = len(graph) - 1

        def explore(node: int, current_path: List[int]):
            if node == destination:
                paths.append(current_path.copy())
                return
            for neighbor in graph[node]:
                current_path.append(neighbor)
                explore(neighbor, current_path)
                current_path.pop()

        explore(0, [0])
        return paths
