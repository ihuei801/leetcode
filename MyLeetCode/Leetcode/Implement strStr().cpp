#if 1
class Solution {
public:
    int strStr(string haystack, string needle) {
        int len1 = haystack.size();
        int len2 = needle.size();
        int count = 0;

        if (haystack == needle || needle.size() == 0)
            return 0;
        for (int i = 0, j = 0; i < len1;)
        {
            if (haystack[i] == needle[j])
            {
                i++, j++, count++;
            }
            else
            {
                i = i - count + 1;
                j = count = 0;
            }

            if (count == len2)
            {
                return i - count;
            }
        }
        return -1;
    }
};
#else
class Solution {
public:
    int strStr(string haystack, string needle) {
        int len1 = haystack.size();
        int len2 = needle.size();

        for (int i = 0; i < len1 - (len2 - 1); i++)
        {
            string sub = haystack.substr(i, len2);
            if (sub == needle)
                return i;
        }
        return -1;
    }
};
#endif