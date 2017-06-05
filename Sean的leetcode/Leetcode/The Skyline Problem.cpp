//https://leetcode.com/discuss/37630/my-c-code-using-one-priority-queue-812-ms
//Time: O(N*logN),  N elements , each element will be pushed (logN) and popped (logN) from priority_queue.
class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int> > res; //X, H
        priority_queue<pair<int, int> > pq; //H, end_X
        int n =  buildings.size();
        int i = 0;

        while(!pq.empty() || i < n)
        {
            int x, h;

            if (i < n)
                x = buildings[i][0]; // x is start_x here.

            //non-overlapped with the current top
            if (i == n || (!pq.empty() && x > pq.top().second))
            {
                //x is end_x here.
                x = pq.top().second;
                //drop the building whose end_x is less that the end_x of the top.
                while (!pq.empty() && pq.top().second <= x)
                    pq.pop();

                h =  pq.empty() ? 0 : pq.top().first;
            }
            //overlapped with the current top
            else
            {
                while (i < n && buildings[i][0] == x)
                {
                    pq.push(make_pair(buildings[i][2], buildings[i][1]));
                    i++;
                }
                h = pq.top().first;
            }

            if (res.empty() || res.back().second != h)
                res.push_back(make_pair(x, h));
        }
        return res;
    }
};