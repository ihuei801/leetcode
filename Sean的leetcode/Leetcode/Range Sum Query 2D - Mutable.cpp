/* Binary Indexed Tree:http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
 * update: O(logn)
 * getSum: O(logn)
 */
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> &matrix) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        org.resize(rows, vector<int>(cols));
        tree.resize(rows + 1, vector<int>(cols + 1));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                update(i, j, matrix[i][j]);
            }
        }
    }

    void update(int row, int col, int val) {
        int rows = org.size();
        int cols = rows? org[0].size() : 0;
        int var = val - org[row][col];
        org[row][col] = val;
        for (int i = row + 1; i <= rows; i += (i & (-i))) {
            for (int j = col + 1; j <= cols; j += (j & (-j))) {
                tree[i][j] += var;
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return sum(row2 + 1, col2 + 1) + sum(row1, col1) - sum(row2 + 1, col1) - sum(row1, col2 + 1);
    }
    int sum(int r, int c) {
        int res = 0;
        for (int i = r; i > 0; i -= (i & (-i))) {
            for (int j = c; j > 0; j -= (j & -j)) {
                res += tree[i][j];
            }
        }
        return res;
    }
    vector<vector<int>> tree;
    vector<vector<int>> org;
};


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.update(1, 1, 10);
// numMatrix.sumRegion(1, 2, 3, 4);
//SumRange:O(logN) update:O(logN)
/*class NumArray {
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
*/

// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> &matrix) {
        int r = matrix.size();
        int c = r == 0? 0 : matrix[0].size();
        this->matrix = matrix;
        rowsum.resize(r, vector<int>(c));
        for (int i = 0; i < r; i++) {
            rowsum[i][0] = matrix[i][0];
            for (int j = 1; j < c; j++) {
                rowsum[i][j] = rowsum[i][j-1] + matrix[i][j];
            }
        }
    }

    void update(int row, int col, int val) {
        int c = rowsum[0].size();
        for (int j = col; j < c; j++) {
            rowsum[row][j] = rowsum[row][j] - matrix[row][col] + val;
        }
        matrix[row][col] = val;
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int r = rowsum.size();
        int c = rowsum[0].size();
        int sum = 0;
        for (int i = row1; i < r && i <= row2; i++) {
            if (col1 == 0) {
                sum += rowsum[i][col2];
            }
            else {
                sum += rowsum[i][col2] - rowsum[i][col1-1];
            }
        }
        return sum;
    }
    vector<vector<int>> matrix;
    vector<vector<int>> rowsum;
};


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.update(1, 1, 10);
// numMatrix.sumRegion(1, 2, 3, 4);