//Two pointers
//Time: O(n), Space: O(1)
string reverseVowels(string s) {
    int n = s.size();
    if (n == 0) return "";
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    int l = 0;
    int r = n - 1;
    while (l < r) {
        if (!vowels.count(s[l])) {
            l++;
        }
        else if (!vowels.count(s[r])) {
            r--;
        }
        else {
            swap(s[l], s[r]);
            l++;
            r--;
        }
    }
    return s;
}
//Sean's solution
class Solution {
public:
    string reverseVowels(string s) {
        int f = 0;
        int e = s.size()-1;
        string vowels = "aeiouAEIOU";
        while(f < e){
            if(vowels.find(s[f]) == string::npos){
                f++;
            }
            else if(vowels.find(s[e]) == string::npos){
                e--;
            }
            else{
                char tmp = s[f];
                s[f] = s[e];
                s[e] = tmp;
                f++;
                e--;
            }
        }
        return s;
    
    }
};