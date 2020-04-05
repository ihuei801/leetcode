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
    //note: the first param should use "&" (called by reference),
    // if not using "&" (i. e. call by value) will cause memory limit exceeding
    TreeNode *buildBST(vector<int> &num, int start, int end)
    {
        TreeNode *left, *right, *parent;
        int mid = (start + end) >> 1;

        if (start > end)
            return NULL;

        left = buildBST(num, start, mid-1);
        parent = new TreeNode(num[mid]);
        parent->left = left;
        right = buildBST(num, mid+1, end);
        parent->right = right;
        return parent;
    }

    TreeNode *sortedArrayToBST(vector<int> &num) {
        return buildBST(num, 0, num.size()-1);
    }
};