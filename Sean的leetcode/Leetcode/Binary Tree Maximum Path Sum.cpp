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
    //1. return value: the max value whose ending point is root. This return value can be used by the parent of current root.
    //2. max_val is current max value.
    int dfs(TreeNode *root, int &max_sum)
    {
        if (!root) return 0;

        int left_res = dfs(root->left, max_sum);
        int right_res = dfs(root->right, max_sum);
        int curr_max = root->val;

        curr_max += left_res > 0 ? left_res : 0;
        curr_max += right_res > 0 ? right_res : 0;
        max_sum = max(max_sum, curr_max);
        int max_child = max(left_res, right_res);
        return max_child > 0 ? root->val + max_child : root->val;
    }

    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        dfs(root, max_sum);
        return max_sum;
    }
};