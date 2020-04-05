#if 1
//Morris traversal, Space : O(1)
//http://www.geeksforgeeks.org/kth-largest-element-in-bst-using-o1-extra-space/
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
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        TreeNode *curr = root;
        int k_val = 0;
        while (curr)
        {
            if (curr->left)
            {
                TreeNode *p = curr->left;
                while (p->right && p->right != curr)
                    p = p->right;

                if (!p->right)
                {
                    p->right = curr;
                    curr = curr->left;
                }
                else
                {
                    p->right = NULL;
                    count++;
                    //note: we need to revert the changes to restore original tree.
                    //so, we cannot early return curr->val here.
                    if (count == k)
                        k_val = curr->val;
                    curr = curr->right;
                }
            }
            else
            {
                count++;
                //note: we need to revert the changes to restore original tree.
                //so, we cannot early return curr->val here.
                if (count == k)
                    k_val = curr->val;
                curr = curr->right;
            }
        }
        return k_val;
    }
};
#elif 1
//Iterative solution: Time: O(n) Space:O(h)
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
    int kthSmallest(TreeNode* root, int k) {
        if (!root || k == 0) return -1;
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr) {
            st.push(curr);
            curr = curr->left;
        }
        int cnt = 0;
        while (!st.empty()) {
            TreeNode* tmp = st.top();
            st.pop();
            cnt++;
            if (cnt == k) {
                return tmp->val;
            }
            if (tmp->right) {
                curr = tmp->right;
                while (curr) {
                    st.push(curr);
                    curr = curr->left;
                }
            }
        }
        return -1;
    }
};
//Sean's version
//iterative solution: Space: O(h)
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
    int kthSmallest(TreeNode* root, int k) {
        vector<TreeNode *> v;
        int count = 0;
        TreeNode *curr = root;

        while (!v.empty() || curr)
        {
            while (curr)
            {
                v.push_back(curr);
                curr = curr->left;
            }
            curr = v.back();
            v.pop_back();
            count++;
            if (count == k)
                return curr->val;
            curr = curr->right;
        }
    }
};
#else
//recursive solution (use inorder)
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
    TreeNode *inorder(TreeNode *root, int &count, int k)
    {
        TreeNode *res;
        if (!root)
            return 0;

        res = inorder(root->left, count, k);
        if (res)
            return res;

        count++;
        if (count == k)
            return root;

        return inorder(root->right, count, k);
    }

    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        TreeNode *res;
        res = inorder(root, count, k);
        return res->val;
    }
};