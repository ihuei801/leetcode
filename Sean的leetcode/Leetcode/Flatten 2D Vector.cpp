class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d):j(0) {
        start = vec2d.begin();
        end = vec2d.end();
    }

    int next() {
        if (hasNext()) {
            return (*start)[j++];
        }
        else {
            return -1;
        }
    }

    bool hasNext() {
        while (start != end) {
            if ((*start).size() == j) {
                j = 0;
                start++;
            }
            else {
                break;
            }
        }
        return start != end;
    }
    vector<vector<int>>::iterator start, end;
    int j;
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */

//https://leetcode.com/discuss/50292/7-9-lines-added-java-and-c-o-1-space
class Vector2D {
public:
    vector<vector<int>>::iterator vcurr, vend;
    int j;
    Vector2D(vector<vector<int>>& vec2d) : j(0) {
        vcurr = vec2d.begin();
        vend = vec2d.end();
    }

    int next() {
        if (hasNext())
            return (*vcurr)[j++];
        return -1;
    }

    bool hasNext() {
        while (vcurr != vend && j == (*vcurr).size())
        {
            vcurr++;
            j = 0;
        }
        return vcurr != vend;
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */