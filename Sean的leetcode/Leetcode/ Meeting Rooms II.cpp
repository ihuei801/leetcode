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
    
    int minMeetingRooms(vector<Interval>& intervals) {
        priority_queue<int, vector<int>, std::greater<int>> pq;
        sort(intervals.begin(), intervals.end(), comp);
        int max_room = 0;
        for (auto e : intervals) {
            while(!pq.empty() && pq.top() <= e.start) {
                pq.pop();
            }
            pq.push(e.end);
            max_room = max(max_room, (int)pq.size());
        }
        return max_room;
    }
};

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
//Time: O(NlogN), Space: O(K), K is max_room
class Solution {
public:
    struct Order
    {
        bool operator() (int a, int b)
        {
            return a > b;
        }
    };

    static bool mysort(Interval &a, Interval &b)
    {
        return a.start < b.start;
    }

    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), mysort);
        priority_queue<int, vector<int>, Order> pq;
        int max_room = 0;

        for (auto i : intervals)
        {
            while (!pq.empty() && i.start >= pq.top())
                pq.pop();

            pq.push(i.end);
            max_room = max(max_room, (int)pq.size());
        }
        return max_room;
    }
};
#elif 1
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
//Time: O(NlogN), because using map to insert (key, value)
//Space: O(N)
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> t_map;
        int max_room = 0;
        int room = 0;
        for (auto i : intervals)
        {
            t_map[i.start]++;
            t_map[i.end]--;
        }
        for (auto m : t_map)
        {
            room += m.second;
            max_room = max(max_room, room);
        }
        return max_room;
    }
};
#endif