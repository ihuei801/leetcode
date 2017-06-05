//BFS
//Time Complexity: O(nlogn) (sorted map)
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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        map<int, vector<int>> table;
        while (!q.empty()) {
            TreeNode* nd = q.front().first;
            int col = q.front().second;
            q.pop();
            table[col].push_back(nd->val);
            if (nd->left) {
                q.push({nd->left, col - 1});
            }
            if (nd->right) {
                q.push({nd->right, col + 1});
            }
        }
        for (auto e: table) {
            res.push_back(e.second);
        }
        return res;
    }
};