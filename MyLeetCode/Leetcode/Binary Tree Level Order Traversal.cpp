#if 1 //iterative solution
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        vector<int> one_row;
        queue<TreeNode *> q;

        if (!root) return res;

        q.push(root);

        while (!q.empty())
        {
            //note: use num to collect the node at the same level.
            int num = q.size();
            for (int i = 0; i < num; i++)
            {
                TreeNode *f = q.front();
                q.pop();
                one_row.push_back(f->val);
                if (f->left)
                    q.push(f->left);
                if (f->right)
                    q.push(f->right);
            }
            res.push_back(one_row);
            one_row.clear();
        }
        return res;
    }
};
#else //recursive solution
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
    void genLevel(TreeNode *root, vector<vector<int>> &res, int level)
    {
        if (!root) return;

        if (level == res.size())
        {
            vector<int> one_level;
            res.push_back(one_level);
        }

        res[level].push_back(root->val);
        genLevel(root->left, res, level+1);
        genLevel(root->right, res, level+1);
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        genLevel(root, res, 0);
        return res;
    }
};
#endif