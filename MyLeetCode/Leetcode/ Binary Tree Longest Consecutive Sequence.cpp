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
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        return dfs(root, NULL, 0);
    }
    int dfs(TreeNode* root, TreeNode* parent, int len) {
        if (parent && parent->val + 1 == root->val) {
            len++;
        }
        else {
            len = 1;
        }
        int maxlen = len;
        if (root->left) {
            maxlen = max(maxlen, dfs(root->left, root, len));
        }
        if (root->right) {
            maxlen = max(maxlen, dfs(root->right, root, len));
        }
        return maxlen;
    }
};
//https://leetcode.com/discuss/66486/c-solution-in-4-lines
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
    int dfs(TreeNode *root, TreeNode *parent, int len)
    {
        if (!root) return len;

        if (parent && parent->val + 1 == root->val)
            len++;
        else
            len = 1;
        return max(len, max(dfs(root->left, root, len), dfs(root->right, root, len)));
    }

    int longestConsecutive(TreeNode* root) {
        return dfs(root, 0, 0);
    }
};