class Solution {
public:
    string simplifyPath(string path) {
        string res;
        vector<string>rs;

        char *p;
        char ptr[path.size()+1];
        strcpy(ptr, path.c_str());

        p = strtok(ptr, "/");
        while (p)
        {
            if (!strcmp("..", p))
            {
                if (!rs.empty())
                    rs.pop_back();
            }
            else if (!strcmp(".", p))
                ;
            else
                rs.push_back(string(p));
            p = strtok(0, "/");
        }

        for (auto r : rs)
            res += "/" + r;

        return res == "" ? "/" : res;
    }
};