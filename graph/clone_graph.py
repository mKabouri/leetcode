# Link: https://leetcode.com/problems/clone-graph/description/

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        graph = Node(val=node.val)
        stack = []
        stack.append(node)

        mapping = {}
        mapping[node] = graph
        while stack != []:
            current_node = stack.pop()
            if current_node.neighbors is not None:
                for neighbor in current_node.neighbors:
                    if neighbor not in mapping:
                        mapping[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)
                    mapping[current_node].neighbors.append(mapping[neighbor])
        return graph
