/*
Step1:Binary Search to find and return the index of interval [s, t] such that s is the largest 'start' that is smaller than n. If no such interval exists, return -1. 
Step2:
After we find this 'index', there are four circumstances:
1.intervals[index] already contains val. Do nothing.
2.val can be merged into intervals[index+1]. Modify intervals[index+1].start to val.
3.val can be merged into intervals[index]. Modify intervals[index].end to val.
4.val can't be merged into either interval. Insert Interval( val, val).
Finally, after inserting val, we need to check whether intervals[index] and intervals[index+1] can be merged.
Time:O(logn)
*/
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class SummaryRanges {
public:
    /** Initialize your data structure here. */
    SummaryRanges() {
        
    }
    
    void addNum(int val) {
        int idx = binarySearch(intervals, val);
        if (idx != -1 && val <= intervals[idx].end) {
            return;
        } else if (idx != intervals.size() - 1 && val + 1 == intervals[idx + 1].start) {
            intervals[idx + 1].start = val;
        } else if (idx != -1 && intervals[idx].end + 1 == val) {
            intervals[idx].end = val;
        } else {
            intervals.insert(intervals.begin() + idx + 1, Interval(val, val));
        }
        if (idx != -1 && intervals[idx].end + 1 == intervals[idx + 1].start){
            intervals[idx].end = intervals[idx + 1].end;
            intervals.erase(intervals.begin() + idx + 1);
        }
        
    }
    
    vector<Interval> getIntervals() {
        return intervals;
    }
private:
    vector<Interval> intervals;
    int binarySearch(vector<Interval>& intervals, int val){
        if (intervals.size() == 0) return -1;
        int left = 0;
        int right = intervals.size() - 1;
        
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (val > intervals[mid].start) {
                left = mid;
            } else if (val < intervals[mid].start) {
                right = mid;
            } else {
                return mid;
            }
        }
        if (val >= intervals[right].start) {
            return right;
        } else if (val >= intervals[left].start) {
            return left;
        } else {
            return -1;
        }
    }
    
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */