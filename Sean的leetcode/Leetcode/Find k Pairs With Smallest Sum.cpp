//https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions
class Solution {
public:
    struct Value{
            int i;
            int j;
            int sum;
            Value(int i, int j, int sum):i(i), j(j), sum(sum){}
    };
    struct comp{
        
        bool operator()(const Value& a, const Value& b) 
        {
            return a.sum > b.sum;
        }
    };
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> res;
        if ( nums1.empty() || nums2.empty() || k < 1 ) return res;  
        priority_queue<Value, vector<Value>, comp> pq;
       
        Value v(0, 0, nums1[0] + nums2[0]);
        pq.push(v);
        while (!pq.empty() && k>0) {
            Value top = pq.top();
            pq.pop();
            k--;
            res.push_back(make_pair(nums1[top.i], nums2[top.j]));
            if (top.j+1 < nums2.size()){
                Value v(top.i, top.j+1, nums1[top.i] + nums2[top.j+1]);
                pq.push(v);
            }
            if (top.i+1 < nums1.size() && top.j == 0){
                Value v(top.i+1, top.j, nums1[top.i+1] + nums2[top.j]);
                pq.push(v);
            }
        }
        return res;
    }
};