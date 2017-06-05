/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    void findPathSum(TreeNode *root, int sum, vector<vector<int> > &res, vector<int> &one_sol)
    {
        if (!root)
            return;
            
        if (root->val == sum && !root->left && !root->right)            
        {
            one_sol.push_back(root->val);
            res.push_back(one_sol);
            one_sol.pop_back();
            return;
        }
        
        one_sol.push_back(root->val);
        findPathSum(root->left, sum-root->val, res, one_sol);
        findPathSum(root->right, sum-root->val, res, one_sol);        
        one_sol.pop_back();                    
    }
    
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<vector<int> >res;
        vector<int>one_sol;
        
        findPathSum(root, sum, res, one_sol);
        return res;
    }
};