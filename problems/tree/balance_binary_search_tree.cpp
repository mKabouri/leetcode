// Link: https://leetcode.com/problems/balance-a-binary-search-tree/description/

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
#include <vector>

class Solution {
public:
    void get_values_in_order(TreeNode *root, vector<int> &values) {
        if (!root) { return; }
        get_values_in_order(root->left, values);
        values.push_back(root->val);
        get_values_in_order(root->right, values);
    }

    TreeNode *build_balanced_search_tree(vector<int> &values, int left, int right) {
        if (left > right) { return NULL; }

        int mid = (left + right)/2;
        TreeNode *root = new TreeNode(values[mid]);
        root->left = build_balanced_search_tree(values, left, mid-1);
        root->right = build_balanced_search_tree(values, mid+1, right);
        return root;
    }

    TreeNode* balanceBST(TreeNode* root) {
        vector<int> values;
        get_values_in_order(root, values);
        return build_balanced_search_tree(values, 0, values.size()-1);
    }
};
