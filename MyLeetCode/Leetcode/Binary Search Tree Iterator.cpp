//Inorder iterative solution
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        TreeNode* curr = root;
        while (curr) {
            stk.push(curr);
            curr = curr->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stk.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode* tmp = stk.top();
        stk.pop();
        if (tmp->right) {
            TreeNode* curr = tmp->right;
            while (curr) {
                stk.push(curr);
                curr = curr->left;
            }
        }
        return tmp->val;
    }
    stack<TreeNode*> stk;
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */


//Sean's solution
//http://www.pixelstech.net/article/1373856647-Binary-tree-iterator-algorithm
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        TreeNode *curr = root;
        while (curr)
        {
            stk.push(curr);
            curr = curr->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stk.empty();
    }

    /** @return the next smallest number */
    int next() {
        if (stk.empty())
        {
            return INT_MIN;
        }
        else
        {
            TreeNode *top = stk.top();
            TreeNode *curr;
            stk.pop();

            if (top->right)
            {
                curr = top->right;
                while (curr)
                {
                    stk.push(curr);
                    curr = curr->left;
                }
            }
            return top->val;
        }
    }
private:
    stack<TreeNode*>stk;
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */