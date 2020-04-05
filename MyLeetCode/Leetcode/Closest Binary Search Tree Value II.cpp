/**
 * The idea is to compare the predecessors and successors of the closest node to the target, 
 * we can use two stacks to track the predecessors and successors, 
 * then like what we do in merge sort, we compare and pick the closest one to the target and put it to the result list.
 * As we know, inorder traversal gives us sorted predecessors, whereas reverse-inorder traversal gives us sorted successors.
 * We can use iterative inorder traversal rather than recursion, but to keep the code clean, here is the recursion version.
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
    void inorder(TreeNode *root, stack<int> &stk, double target, int reverse)
    {
        if (!root) return;

        inorder(reverse ? root->right : root->left, stk, target, reverse);

        if ((!reverse && root->val > target)
            || (reverse && root->val <= target))
            return;

        stk.push(root->val);

        inorder(reverse ? root->left : root->right, stk, target, reverse);
    }

    vector<int> closestKValues(TreeNode* root, double target, int k) {
        
        vector<int> res;
        if (!root || !k) return res;
        stack<int> min_stk, max_stk;
        inorder(root, min_stk, target, 0);
        inorder(root, max_stk, target, 1);
        while (k--)
        {
            if (min_stk.empty())
            {
                res.push_back(max_stk.top());
                max_stk.pop();
            }
            else if (max_stk.empty())
            {
                res.push_back(min_stk.top());
                min_stk.pop();
            }
            else
            {
                if (abs(min_stk.top()-target) < abs(max_stk.top()-target))
                {
                    res.push_back(min_stk.top());
                    min_stk.pop();
                }
                else
                {
                    res.push_back(max_stk.top());
                    max_stk.pop();
                }
            }
        }
        return res;
    }
};