//https://leetcode.com/discuss/13610/share-my-concise-c-solution-less-than-20-lines
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i, k, len;
        string str;

        for (i = 0; i < words.size(); i += k)
        {
            //k+1 is the number of word in one line. So k is the minimum number of spaces (at least one sapce between two words.)
            for (len = 0, k = 0; i + k < words.size() && len + k + words[i+k].size() <= maxWidth; k++)
                len += words[i+k].size();

            str = words[i];
            for (int j = 1; j < k; j++)
            {
                //the last line: left justified
                if (i + k == words.size())
                    str += " ";
                //other lines: fully justified
                else
                {
                    //if j < (L-len)%(k-1), which is one the left side, need one more space.
                    str += string((maxWidth - len)/(k - 1) + (j <= ((maxWidth - len)%(k-1))), ' ');
                }
                str += words[i+j];
            }
            str += string(maxWidth - str.size(), ' ');
            res.push_back(str);
        }
        return res;
    }
};