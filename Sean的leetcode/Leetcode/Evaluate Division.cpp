class Solution {
public:
    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) {
        unordered_map<string, unordered_map<string, double>> table;
        for (int i = 0; i < equations.size(); i++) {
            table[equations[i].first][equations[i].second] = values[i];
            table[equations[i].second][equations[i].first] = 1.0 / values[i];
        }
        vector<double> res(queries.size());
        
        int i = 0;
        for (auto q : queries) {
            unordered_set<string> visit;
            double ans = find_res(q.first, q.second, table, visit);
            res[i++] = ans == NULL? -1.0 : ans;
        }
        return res;
    }
    
    double find_res(string num, string deno, unordered_map<string, unordered_map<string,double>>& table, unordered_set<string>& visit) {
        string key = num + ":" + deno;
        if (visit.count(key)) return NULL;
        visit.insert(key);
        if (!table.count(num) || !table.count(deno)) return NULL;
        if (num == deno) return 1.0;
        
        unordered_map<string, double> paths = table[num];
        if (table[num].count(deno)) {
            return table[num][deno];
        }
        for (auto p : paths) {
            double ans = find_res(p.first, deno, table, visit);
            if (ans != NULL){
                return p.second * ans;
            } 
        }
        visit.erase(key);
        return NULL;
    
        
    }
    
};