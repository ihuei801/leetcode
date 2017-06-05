/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#if 1 // DFS
/* 1. traverse (right subtree first) root->right->left.
   2. target_level is the output level.
   3. curr_level is the level of the root.
 */
class Solution {
public:
    void dfs(TreeNode *root, vector<int> &res, int level)
    {
        if (!root) return;

        if (level == res.size())
            res.push_back(root->val);

        dfs(root->right, res, level+1);
        dfs(root->left, res, level+1);
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root, res, 0);
        return res;
    }
};
#else //BFS
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        queue<pair<int, TreeNode*> >bfs;
        vector<int>res;
        pair<int, TreeNode*>node;

        if (!root) return res;

        bfs.push(make_pair(0, root));

        while (!bfs.empty())
        {
            node = bfs.front();

            if (node.second->left)
                bfs.push(make_pair(node.first+1, node.second->left));

            if (node.second->right)
                bfs.push(make_pair(node.first+1, node.second->right));

            bfs.pop();

            if (!bfs.empty() && bfs.front().first != node.first)
                res.push_back(node.second->val);
        }
        res.push_back(node.second->val);
        return res;
    }
};
#endif