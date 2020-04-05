//https://leetcode.com/discuss/35401/c-dfs-backtracking-and-bfs-indegree-methods
class Solution {

public:
    //dfs: flagged: ever start from this vertex. visited: visited in this current traverse.
    bool hasCycle(int start_index, unordered_map<int, vector<int>> &neighbor, vector<int> &flagged, vector<int> &visited)
    {
        if (flagged[start_index])
            return false;
        flagged[start_index] = 1;
        visited[start_index] = 1;
        for (int i = 0; i < neighbor[start_index].size(); i++)
        {
            int idx = neighbor[start_index][i];
            if (visited[idx])
                return true;
            if (hasCycle(idx, neighbor, flagged, visited))
                return true;
        }
        visited[start_index] = 0;
        return false;
    }

    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        unordered_map<int, vector<int>>neighbor;
        vector<int> flagged(numCourses, 0);
        vector<int> visited(numCourses, 0);

        for (int i = 0; i < prerequisites.size(); i++)
            neighbor[prerequisites[i].second].push_back(prerequisites[i].first);

        for (int i = 0; i < numCourses; i++)
        {
            if (!flagged[i])
            {
                if (hasCycle(i, neighbor, flagged, visited))
                    return false;
            }
        }
        return true;
    }

};