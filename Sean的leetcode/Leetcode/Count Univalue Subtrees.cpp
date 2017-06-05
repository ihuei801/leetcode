//https://leetcode.com/discuss/52210/c-one-pass-recursive-solution
//Time: O(n)
class Solution {
public:
    bool countUnivalTree(TreeNode *root, int &count)
    {
        if (!root) return true;

        bool uni_left = countUnivalTree(root->left, count);
        bool uni_right = countUnivalTree(root->right, count);

        if ((uni_left && uni_right)
            && (!root->left || root->left->val == root->val)
            && (!root->right || root->right->val == root->val))
        {
            count++;
            return true;
        }
        return false;
    }

    int countUnivalSubtrees(TreeNode* root) {
        int count = 0;
        countUnivalTree(root, count);
        return count;
    }
};
