/* 1.Sort the array. Ascend on width and descend on height if width are same. 
 * (descending height because if the width is the same, one cannot contain the other even if its height is greater)
 * 2.Find the longest increasing subsequence based on height.
 * ref: http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
 * Time Complexity: O(nlogn)
 * user lower bound to find the element that is smallest larger than an element
 */
class Solution {
public:
    static bool comp (pair<int,int>& a, pair<int, int>& b) {
        if (a.first != b.first) {
            return b.first > a.first;
        }
        else {
            return b.second < a.second;
        }
    }
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        int n = envelopes.size();
        if (n <= 1) return n;
        sort(envelopes.begin(), envelopes.end(), comp); 
        vector<int> ends;
        for (auto e : envelopes) {
            if (ends.empty()) {
                ends.push_back(e.second);
            }
            else if (e.second < ends[0]) {
                ends[0] = e.second;
            }
            else if (e.second > ends.back()) {
                ends.push_back(e.second);
            }
            else {
                auto it = lower_bound(ends.begin(), ends.end(), e.second);
                (*it) = e.second;
                
            }
        }
        return ends.size();
    }
};
//Use binary search to find an element that is smallest larger than an element
class Solution {
public:
    static bool cmp(pair<int, int> a, pair<int, int> b){
        if (a.first != b.first) {
            return a.first < b.first;
        }
        else {
            return a.second > b.second;
        }
    }
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        int size = envelopes.size();
        if (size <= 1) return size;
        sort(envelopes.begin(), envelopes.end(), cmp);
        vector<int> ends;
        for (auto e: envelopes) {
            if (ends.empty()) {
                ends.push_back(e.second);
            } 
            else if (e.second < ends[0]){
                ends[0] = e.second;
            }
            else if (e.second > ends.back()){
                ends.push_back(e.second);
            }
            else{
                int l = 0;
                int r = ends.size() - 1;
                while (l + 1 < r) {
                    int mid = l + (r - l)/2;
                    if (ends[mid] >= e.second) {
                        r = mid;
                    }
                    else{
                        l = mid;
                    }
                }
                if (ends[l] >= e.second) {
                    ends[l] = e.second;
                }
                else {
                    ends[r] = e.second;
                }
            }
        }
        return ends.size();
    }
};