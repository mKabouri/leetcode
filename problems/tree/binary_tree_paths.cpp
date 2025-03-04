// Link: https://leetcode.com/problems/binary-tree-paths/description/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void preorder(TreeNode *node, string cur_str, vector<string> &root2leaf_paths) {
        if (!node) { return; }

        cur_str += (cur_str.empty() ? "" : "->") + to_string(node->val);

        if (!node->left && !node->right) {
            root2leaf_paths.push_back(cur_str);
            return;
        }
        preorder(node->left, cur_str, root2leaf_paths);
        preorder(node->right, cur_str, root2leaf_paths);

    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> root2leaf_paths;
        string cur_str = "";
        preorder(root, cur_str, root2leaf_paths);
        return root2leaf_paths;
    }
};
