class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        visited = set()
        def remove_path_start_with(node: int):
            for path in paths[:]:
                if path[0] == node:
                    paths.remove(path)

        def dfs_paths(node: int, path: List[int]):
            if graph[node] == [] and len(path) > 1:
                paths.append(path.copy())
            for neighbor in graph[node]:
                if neighbor in visited:
                    remove_path_start_with(neighbor)
                visited.add(neighbor)
                path.append(neighbor)
                dfs_paths(neighbor, path)
                path.pop()

        n = len(graph)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                path = [node]
                dfs_paths(node, path)
        return paths
