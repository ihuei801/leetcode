//https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    void serial(TreeNode *root, string &res)
    {
        if (!root)
        {
            res += "#,";
            return;
        }
        res += to_string(root->val) + ",";
        serial(root->left, res);
        serial(root->right, res);
    }

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res;
        serial(root, res);
        return res;
    }

    TreeNode *deserial(string &data, int &pos)
    {
        if (pos == data.size())
            return 0;
        int end = data.find_first_of(',', pos);
        string s = data.substr(pos, end - pos);
        pos = end + 1;
        if (s == "#")
            return 0;
        TreeNode *root = new TreeNode(stoi(s));
        root->left = deserial(data, pos);
        root->right = deserial(data, pos);
        return root;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return deserial(data, pos);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));