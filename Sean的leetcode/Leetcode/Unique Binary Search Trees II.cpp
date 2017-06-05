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
    vector<TreeNode*> gen(int start, int end)
    {
        vector<TreeNode *>res;

        if (start > end)
        {
            res.push_back(0);
            return res;
        }
        for (int i = start; i <= end; i++)
        {
            vector<TreeNode *> res_l = gen(start, i-1);
            vector<TreeNode *> res_r = gen(i+1, end);

            for (auto l : res_l)
                for (auto r : res_r)
                {
                    TreeNode *root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
        }
        return res;
    }

    vector<TreeNode*> generateTrees(int n) {
        return gen(1, n);
    }
};