# Link: https://leetcode.com/problems/keys-and-rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Connected Graph
        n = len(rooms)
        visited = set()
        visited.add(0)
        def dfs(room: int):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        dfs(0)
        if len(visited) == n:
            return True
        return False
