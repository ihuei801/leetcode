#if 1 //BFS
//http://en.wikipedia.org/wiki/Topological_sorting
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> res;
        unordered_map<int, vector<int>> out_degree;
        vector<int> in_degree(numCourses, 0);
        queue<int> zero_degree;

        // 1 -> 2,  means 1 is pre-requisite, this is 1's outdegree and 2's indegree
        for (int i = 0; i < prerequisites.size(); i++)
        {
            out_degree[prerequisites[i].second].push_back(prerequisites[i].first);
            in_degree[prerequisites[i].first]++;
        }

        for (int i = 0; i < numCourses; i++)
        {
            if (in_degree[i] == 0)
                zero_degree.push(i);
        }

        while (!zero_degree.empty())
        {
            int f = zero_degree.front();
            res.push_back(f);
            zero_degree.pop();

            vector<int> out = out_degree[f];
            for (auto i : out)
            {
                in_degree[i]--;
                if (in_degree[i] == 0)
                    zero_degree.push(i);
            }
        }

        if (res.size() != numCourses)
            res.clear();
        return res;
    }
};
#elif 1 //DFS
class Solution {
public:
    bool hasCycle(int idx, unordered_map<int, vector<int>> &out_degree, unordered_set<int> &on_path, unordered_set<int> &visited, vector<int> &res)
    {
        if (visited.count(idx))
            return false;

        visited.insert(idx);
        on_path.insert(idx);

        for (auto n : out_degree[idx])
        {
            if (on_path.count(n))
                return true;
            if (hasCycle(n, out_degree, on_path, visited, res))
                return true;
        }
        on_path.erase(idx);
        //idx is push to res after its children. That's why we need reverse(res.begin(), res.end()) before main() returns.
        res.push_back(idx);
        return false;
    }


    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        unordered_map<int, vector<int>> out_degree;
        vector<int> res;
        unordered_set<int> on_path, visited;

        for (auto p : prerequisites)
            out_degree[p.second].push_back(p.first);

        for (int i = 0; i < numCourses; i++)
            if (hasCycle(i, out_degree, on_path, visited, res))
                return {};
        reverse(res.begin(), res.end());
        return res;
    }
};
#endif