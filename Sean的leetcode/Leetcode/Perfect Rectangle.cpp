/* Time: O(n)
 * The right answer must satisfy two conditions:
 * (1) The large rectangle area should be equal to the sum of small rectangles
 * (2) count of all points except the four corner points of the perfect rectangle should be even, 
 *     and the four corner points of the perfect rectangle points should appear once
 */
class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        int n = rectangles.size();
        if (n == 0) return false;
        int x1 = INT_MAX, y1 = INT_MAX;
        int x2 = INT_MIN, y2 = INT_MIN;
        unordered_set<string> points;
        int sum = 0;
        for (auto r : rectangles) {
            x1 = min(x1, r[0]);
            y1 = min(y1, r[1]);
            x2 = max(x2, r[2]);
            y2 = max(y2, r[3]);
            sum += (r[3] - r[1]) * (r[2] - r[0]);
            
            vector<string> p = {to_string(r[0]) + "," + to_string(r[1]), to_string(r[0]) + "," + to_string(r[3]), to_string(r[2]) + "," + to_string(r[1]), to_string(r[2]) + "," + to_string(r[3])};
            for (auto e : p) {
                if (points.count(e)) {
                    points.erase(e);
                }
                else {
                    points.insert(e);
                }
            }
        }
        if (!points.count(to_string(x1) + "," + to_string(y1)) || !points.count(to_string(x1) + "," + to_string(y2)) || !points.count(to_string(x2) + "," + to_string(y1)) || !points.count(to_string(x2) + "," + to_string(y2)) || points.size() != 4) return false;
        return (y2 - y1) * (x2 - x1) == sum;
        
    }
};
//version2
class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        int x1 = INT_MAX, y1 = INT_MAX;
        int x2 = INT_MIN, y2 = INT_MIN;
        int sum = 0;
        unordered_set<string> appear;
        for (auto rectangle : rectangles) {
            x1 = min(x1, rectangle[0]);
            y1 = min(y1, rectangle[1]);
            x2 = max(x2, rectangle[2]);
            y2 = max(y2, rectangle[3]);
            sum += (rectangle[3] - rectangle[1]) * (rectangle[2] - rectangle[0]);
            string ld = to_string(rectangle[0]) + "," + to_string(rectangle[1]);
            string lu = to_string(rectangle[0]) + "," + to_string(rectangle[3]);
            string rd = to_string(rectangle[2]) + "," + to_string(rectangle[1]);
            string ru = to_string(rectangle[2]) + "," + to_string(rectangle[3]);
            if (appear.count(ld)) {
                appear.erase(ld);
            } else {
                appear.insert(ld);
            }
            if (appear.count(lu)) {
                appear.erase(lu);
            } else {
                appear.insert(lu);
            }
            if (appear.count(rd)) {
                appear.erase(rd);
            } else {
                appear.insert(rd);
            }
            if (appear.count(ru)) {
                appear.erase(ru);
            } else {
                appear.insert(ru);
            }
            
        }
        if (!appear.count(to_string(x1) + "," + to_string(y1)) || !appear.count(to_string(x1) + "," + to_string(y2)) || !appear.count(to_string(x2) + "," + to_string(y1))  || !appear.count(to_string(x2) + "," + to_string(y2)) || appear.size() != 4) return false;
        return sum == (y2 - y1) * (x2 - x1);
    }
};