class Solution {
public:
    void reverse(string &s, int left, int right)
    {
        while (left < right)
            swap(s[left++], s[right--]);
    }

    void reverseWords(string &s) {
        int n = s.size();
        reverse(s, 0, n-1);
        int left = 0;
        int right = 0;
        while (right <= n)
        {
            if (right == n || s[right] == ' ')
            {
                reverse(s, left, right-1);
                left = right = right + 1;
            }
            right++;
        }
    }
};