//Binary Search O(mlogn + nlogm)
//Search for the boundary, find the first line that contains one
class Solution {
public:
    vector<vector<char>> img;
    int minArea(vector<vector<char>>& image, int x, int y) {
        img = image;
        int rows = image.size();
        int cols = rows? image[0].size() : 0;
        if (!rows || !cols) return 0;
        int up = binarysearch(0, x, 0, cols-1, 0);
        int down = binarysearch(x, rows-1, 0, cols-1, 1);
        int left = binarysearch(0, y, up, down, 2);
        int right = binarysearch(y, cols-1, up, down, 3);
        return (down - up + 1) * (right - left + 1);
    }
    int binarysearch(int l, int r, int low, int high, int dir) {
        
        if (dir == 0) {
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                int j;
                for (j = low; j <= high && img[mid][j] != '1'; j++);
                if (j <= high) {
                    r = mid;
                }
                else {
                    l = mid;
                }
            }
            int j;
            for (j = low; j <= high && img[l][j] != '1'; j++);
            return j <= high? l : r;
        }
        else if (dir == 1) {
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                int j;
                for (j = low; j <= high && img[mid][j] != '1'; j++);
                if (j <= high) {
                    l = mid;
                }
                else {
                    r = mid;
                }
            }
            int j;
            for (j = low; j <= high && img[r][j] != '1'; j++);
            return j <= high? r : l;
        }
        else if (dir == 2) {
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                int i;
                for (i = low; i <= high && img[i][mid] != '1'; i++);
                if (i <= high) {
                    r = mid;
                }
                else {
                    l = mid;
                }
            }
            int i;
            for (i = low; i <= high && img[i][l] != '1'; i++);
            return i <= high? l : r;
        }
        else {
            while (l + 1 < r) {
                int mid = l + (r - l) / 2;
                int i;
                for (i = low; i <= high && img[i][mid] != '1'; i++);
                if (i <= high) {
                    l = mid;
                }
                else {
                    r = mid;
                }
            }
            int i;
            for (i = low; i <= high && img[i][r] != '1'; i++);
            return i <= high? r : l;
        }
    }
};
//DFS, Time: O(mn)
class Solution {
public:
    void dfs(vector<vector<char>>& image, int row, int col, int &min_row, int &max_row, int &min_col, int &max_col)
    {
        int dir[] = {0, 1, 0, -1, 0};
        int M_row = image.size();

        if (!M_row) return;

        int M_col = image[0].size();

        if (row < 0 || col < 0 || row >= M_row || col >= M_col)
            return;

        if (image[row][col] == '1')
        {
            if (row < min_row) min_row = row;
            if (row > max_row) max_row = row;
            if (col < min_col) min_col = col;
            if (col > max_col) max_col = col;
            image[row][col] = 0;
            for (int i = 0; i < 4; i++)
                dfs(image, row+dir[i], col+dir[i+1], min_row, max_row, min_col, max_col);
        }
    }

    int minArea(vector<vector<char>>& image, int x, int y) {
        int min_row = INT_MAX, min_col = INT_MAX;
        int max_row = INT_MIN, max_col = INT_MIN;

        int M_row = image.size();

        if (!M_row) return 0;

        dfs(image, x, y, min_row, max_row, min_col, max_col);

        return (max_row - min_row + 1) * (max_col - min_col + 1);
    }
};