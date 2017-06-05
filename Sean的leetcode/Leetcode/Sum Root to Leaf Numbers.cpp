/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode *root, int sum, int &total_sum)
    {
        if (!root) return;

        sum = sum * 10 + root->val;

        if (!root->left && !root->right)
        {
            total_sum += sum;
            return;
        }
        dfs(root->left, sum, total_sum);
        dfs(root->right, sum, total_sum);
    }

    int sumNumbers(TreeNode* root) {
        int total = 0;
        dfs(root, 0, total);
        return total;
    }
};