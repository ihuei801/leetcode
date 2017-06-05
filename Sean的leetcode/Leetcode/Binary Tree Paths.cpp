//Back Tracking
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if (!root) return res;
        string one_sol;
        dfs(root, one_sol, res);
        return res;
    }
    void dfs(TreeNode* root, string one_sol, vector<string>& res) {
        if (!root) return;
        if (!one_sol.empty()) {
            one_sol += "->";
        }
        one_sol += to_string(root->val);
        if (!root->left && !root->right) {
            res.push_back(one_sol);
            return;
        }
        if (root->left) {
            dfs(root->left, one_sol, res);
        }
        if (root->right) {
            dfs(root->right, one_sol, res);
        }
        
    }
};

//Sean's solution
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string>left, right, res;

        if (!root)
            return res;

        left = binaryTreePaths(root->left);
        right = binaryTreePaths(root->right);

        if (left.empty() && right.empty())
        {
            res.push_back(to_string(root->val));
            return res;
        }

        for (auto &p : left)
            res.push_back(to_string(root->val)+"->"+p);

        for (auto &p : right)
            res.push_back(to_string(root->val)+"->"+p);
        return res;
    }
};