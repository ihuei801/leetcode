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
    void genLevel(TreeNode *root, vector<vector<int> > &res, int level)
    {
        if (!root) return;

        if (res.size() == level)
        {
            vector<int> one_level;
            res.push_back(vector<int>());
        }
        res[level].push_back(root->val);
        genLevel(root->left, res, level+1);
        genLevel(root->right, res, level+1);
    }

    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int> > res;
        genLevel(root, res, 0);
        reverse(res.begin(), res.end());
        return res;
    }
};