// Link: https://leetcode.com/problems/add-one-row-to-tree/description/

class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {  
        if (depth == 1 && root.right == null && root.left == null) {
            return new TreeNode(val, root, null);
        }
        if (depth == 1) {
            return new TreeNode(val, root, null);   
        }
        if (depth == 2 && root != null) {
            return new TreeNode(root.val, new TreeNode(val, root.left, null), new TreeNode(val, null, root.right));
        }
        else if (root == null) {
            return null;
        }
        else {
            return new TreeNode(root.val, addOneRow(root.left, val, depth-1), addOneRow(root.right, val, depth-1)); 
        }
    }   
}
