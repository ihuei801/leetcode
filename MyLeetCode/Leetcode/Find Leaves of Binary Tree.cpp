//DFS
//Time Complexity:O(n)
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

    vector<vector<int>> findLeaves(TreeNode* root) {
        dfs(root);
        return re;
    }
    int dfs(TreeNode* root) {
        if (!root) {
            return -1;
        } 
        int level = 1 + max(dfs(root->left), dfs(root->right));
        if (re.size() == level) {
            re.push_back({});
        }
        re[level].push_back(root->val);
        return level;
    }
private:
    vector<vector<int>> re;
};