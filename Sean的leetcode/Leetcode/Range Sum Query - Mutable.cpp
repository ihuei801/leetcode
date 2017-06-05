//SumRange:O(logN) update:O(logN)
class NumArray {
struct SegmentTreeNode{
    int start, end;
    int sum;
    SegmentTreeNode* left;
    SegmentTreeNode* right;
    SegmentTreeNode(int s, int e) : start(s), end(e), sum(0), left(NULL), right(NULL){}
};
public:
    NumArray(vector<int> &nums) {
            root = buildTree(nums, 0, nums.size() - 1);
    }
    SegmentTreeNode* buildTree(vector<int>& nums, int start, int end){
        if (start > end) return NULL;
        SegmentTreeNode* root = new SegmentTreeNode(start, end);
        if (start == end){
            root->sum = nums[start];
        } else {
            int mid = start + (end - start) / 2;
            root->left = buildTree(nums, start, mid);
            root->right = buildTree(nums, mid + 1, end);
            root->sum = root->left->sum + root->right->sum;
        }
        return root;
    }

    void update(int i, int val) {
        update(i, val, root);
    }
    void update(int i, int val, SegmentTreeNode* root){
        if (!root) return;
        if (root->start == root->end) {
            root->sum = val;
        } else {
            int mid = root->start + (root->end - root->start) / 2;
            if (i <= mid){
                update(i, val, root->left);
            } else {
                update(i, val, root->right);
            }
            root->sum = root->left->sum + root->right->sum;
        }
    }

    int sumRange(int i, int j) {
        return sumRange(i, j, root);
    }
    int sumRange(int i, int j, SegmentTreeNode* root){
        if (!root) return 0;
        if (i == root->start && j == root->end) {
            return root->sum;
        } else {
            int mid = root->start + (root->end - root->start) / 2;
            if (j <= mid){
                return sumRange(i, j, root->left);
            } else if (i > mid){
                return sumRange(i, j, root->right);
            } else {
                return sumRange(i, mid, root->left) + sumRange(mid + 1, j, root->right);
            }
        }
    }
private:
    SegmentTreeNode* root;
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);