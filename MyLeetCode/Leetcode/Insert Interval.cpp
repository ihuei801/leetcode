#if 1
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
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> res;
        int n = intervals.size();
        if (n == 0) {
            res.push_back(newInterval);
            return res;
        }
        for (int i = 0; i < n; i++)
        {
            if (intervals[i].end < newInterval.start)
                res.push_back(intervals[i]);
            else if (newInterval.end < intervals[i].start)
            {
                res.push_back(newInterval);
                newInterval = intervals[i];
            }
            //overlapped
            else
            {
                newInterval.start = min(newInterval.start, intervals[i].start);
                newInterval.end = max(newInterval.end, intervals[i].end);
            }
        }
        res.push_back(newInterval);
        return res;
    }
};
#else
//no extra space but time limit exceed. guess resulting from erase() and insert();
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
#define MIN(a, b) ((a < b) ? (a) : (b))
#define MAX(a, b) ((a > b) ? (a) : (b))
class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval>::iterator it = intervals.begin();

        while (it != intervals.end())
        {
            if (it->end < newInterval.start)
                it++;
            else if (newInterval.end < it->start)
            {
                intervals.insert(it, newInterval);
                return intervals;
            }
            else
            {
                newInterval.start = MIN(newInterval.start, it->start);
                newInterval.end   = MAX(newInterval.end, it->end);
                it = intervals.erase(it);
            }
        }
        intervals.insert(it, newInterval);
        return intervals;
    }
};