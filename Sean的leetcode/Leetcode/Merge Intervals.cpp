#if 1 //Time: O(NlogN+N)
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool comp(Interval& a, Interval& b) {
        return b.start > a.start;
    }
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;
        int n = intervals.size();
        if (n == 0) return res;
        sort(intervals.begin(), intervals.end(), comp);
        Interval pre = intervals[0];
        for (int i = 1; i < n; i++) {
            if (pre.end < intervals[i].start) {
                res.push_back(pre);
                pre = intervals[i];
            }
            else{
                pre.start = min(pre.start, intervals[i].start);
                pre.end = max(pre.end, intervals[i].end);
            }
        }
        res.push_back(pre);
        return res;
        
    }
};
//Sean's solution
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool cmp(Interval &a, Interval &b)
    {
        return a.start < b.start;
    }

    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;

        //O(NlogN)
        sort(intervals.begin(), intervals.end(), cmp);

        if (!intervals.size()) return res;

        Interval itl = intervals[0];

        //O(N)
        for (int i = 1; i < intervals.size(); i++)
        {
            int start = intervals[i].start;
            int end = intervals[i].end;

            if (itl.end < start)
            {
                res.push_back(itl);
                itl.start = start;
                itl.end = end;
            }
            else
            {
                itl.start = min(start, itl.start);
                itl.end = max(end, itl.end);
            }
        }
        res.push_back(itl);
        return res;
    }
};
#elif 1 //Time: O(N^2)
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval)
    {
        vector<Interval> res;

        for (int i = 0; i < intervals.size(); i++)
        {
            if (newInterval.end < intervals[i].start)
            {
                res.push_back(newInterval);
                newInterval.start = intervals[i].start;
                newInterval.end = intervals[i].end;
            }
            else if (intervals[i].end < newInterval.start)
            {
                res.push_back(intervals[i]);
            }
            else
            {
                newInterval.start = min(newInterval.start, intervals[i].start);
                newInterval.end = max(newInterval.end, intervals[i].end);
            }
        }
        res.push_back(newInterval);
        return res;
    }

    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> res;

        if (intervals.size() == 0) return res;

        for (int i = 0; i < intervals.size(); i++)
            res = insert(res, intervals[i]);

        return res;
    }
};
#endif