//O(n)
class Solution {
public:
    bool isStrobogrammatic(string num) {
        int n = num.size();
        if (n == 0) return true;
        unordered_map<char, char> table = {{'0', '0'}, {'1', '1'}, {'8', '8'}, {'6', '9'}, {'9', '6'}};
        int l = 0;
        int r = n-1;
        while (l <= r) {
            if (!table.count(num[l]) || table[num[l]] != num[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};

class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char> table = {{'0','0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
        int n = num.size();
        int l = 0;
        int r = n - 1;
        
        while(l <= r) {
            if (!table.count(num[l]) || table[num[l++]] != num[r--]) {
                return false;
            }
        }
        return true;
        
     }
};

//Sean's solution
//http://www.cnblogs.com/jcliBlogger/p/4708243.html
class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char> n_map;
        n_map['0'] = '0';
        n_map['1'] = '1';
        n_map['6'] = '9';
        n_map['8'] = '8';
        n_map['9'] = '6';
        int n = num.size();
        int left = 0;
        int right = n - 1;
        while (left <= right)
        {
            if (!n_map.count(num[left]) || n_map[num[left++]] != num[right--])
                return false;
        }
        return true;
    }
};