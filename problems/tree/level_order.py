# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def bfs(self, root, save_dict, level):
        if root == None:
            return save_dict
        else:
            save_dict[level].append(root.val)
            level += 1
            self.bfs(root.left, save_dict, level)
            self.bfs(root.right, save_dict, level)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs_res = defaultdict(list)
        self.bfs(root, bfs_res, 0)
        return list(bfs_res.values())
