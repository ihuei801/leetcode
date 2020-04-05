sclass Solution {
public:
    void reverseWords(string &s) {
        if (s.empty()) return;
        reverse(s.begin(), s.end());
        int n = s.size();
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == ' ') continue;
            if (idx != 0) s[idx++] = ' ';
            int j = i;
            for (; j < n && s[j] != ' '; j++) {
                s[idx++] = s[j];
            }
            reverse(s.begin() + idx - (j-i), s.begin()+idx);
            i = j;
        }
        s.erase(s.begin() + idx, s.end());
    }
};
//1. reverse whole string
//2. reverse every word
class Solution {
public:
    void reverse_str(string &s, int left, int right)
    {
        while (left < right)
            swap(s[left++], s[right--]);
    }

    void reverseWords(string &s) {
        int i, j, start = 0;
        int pos = 0;

        reverse_str(s, 0, s.size()-1);

        for (i = 0; i < s.size();)
        {
            if (s[i] == ' ')
            {
                i++;
                continue;
            }
            for (j = i + 1; j < s.size() && s[j] != ' '; j++)
                ;
            j--;

            if (pos)
                s[pos++] = ' ';

            //no leading space
            if (pos == i)
            {
                reverse_str(s, i, j);
                pos = j + 1;
            }
            //with leading space
            else
            {
                for (int k = j, p = pos; k >= i && p < k;)
                    swap(s[p++], s[k--]);
                pos += j - i + 1;
            }
            i = j + 1;
        }
        s.resize(pos);
    }
};
//pure C version
#if 0
int reverse(char *start, char *end)
{
    char temp;

    if (!start)
        return -1;


    while (start < end)
    {
        temp = *end;
        *end = *start;
        *start = temp;
        start++;
        end--;
    }
    return 0;
}

int reverse_words(char *str)
{
    char *curr = str;
    char *end = str;
    char *start = 0;

    if (!str)
        return -1;

    while (*end)
        end++;

    reverse(str, end-1);

    while (*curr)
    {
        if (*curr == ' ')
        {
            if (start)
            {
                assert(*start != ' ');
                reverse(start, curr-1);
                start = 0;
            }
        }
        //this implies *curr is not equal to ' '
        else if (!start)
            start = curr;

        curr++;
    }
    reverse(start, curr-1);
    return 0;
}

#endif