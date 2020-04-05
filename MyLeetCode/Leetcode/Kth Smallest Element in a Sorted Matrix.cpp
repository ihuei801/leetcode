/* Use a priority queue to go through the matrix
 * increase when going right or going down
 * Time Complexity: O(klogk)
 */
class Solution {
public:
    struct Element {
        int r;
        int c;
        int val;
        Element(int a, int b, int v): r(a), c(b), val(v){}
    };
    class comp {
        public:
            bool operator() (const Element& a, const Element& b) {
                return a.val > b.val;
            }
    };
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int rows = matrix.size();
        int cols = rows? matrix[0].size() : 0;
        int bound = k > cols? cols : k;
        priority_queue<Element, vector<Element>, comp> pq;
        for (int j = 0; j < bound; j++) {
            Element e(0, j, matrix[0][j]);
            pq.push(e);
        }
        for (int i = 0; i < k - 1; i++) {
            Element top = pq.top();
            pq.pop();
            if (top.r == rows - 1) continue;
            pq.push(Element(top.r + 1, top.c, matrix[top.r + 1][top.c]));
            
        }
        return pq.top().val;
    }
};