#if 1
class Solution {
public:
    int compareVersion(string version1, string version2) {
        char *token1, *token2;
        vector<int>num1;
        vector<int>num2;
        int i;

        char *str1 = new char [version1.size()+1];
        strcpy (str1, version1.c_str());

        char *str2 = new char [version2.size()+1];
        strcpy (str2, version2.c_str());

        token1 = strtok(str1, ".");
        while (token1)
        {
            num1.push_back(atoi(token1));
            token1 = strtok(NULL, ".");
        }

        token2 = strtok(str2, ".");
        while (token2)
        {
            num2.push_back(atoi(token2));
            token2 = strtok(NULL, ".");
        }

        for (i = 0; i < num1.size() && i < num2.size(); i++)
        {
            if (num1[i] > num2[i])
                return 1;
            if (num1[i] < num2[i])
                return -1;
        }

        if (i != num1.size() && num1[i] > 0 && i == num2.size())
            return 1;
        if (i == num1.size() && i != num2.size() && num2[i] > 0)
            return -1;

        return 0;
    }
};
#else //recrusive solution
class Solution {
public:
    int compareVersion(string &v1, string &v2, int i1, int i2){
        int n1 = 0, n2 = 0;
        int j1 = i1, j2 = i2;

        if(i1 == v1.size() && i2 == v2.size())
            return 0;

        while(j1 < v1.size() && v1[j1] != '.') n1 = 10*n1 + v1[j1++] - '0';
        while(j2 < v2.size() && v2[j2] != '.') n2 = 10*n2 + v2[j2++] - '0';

        if(n1 > n2)
            return 1;
        else if(n1 < n2)
            return -1;
        else
            return compareVersion(v1, v2, ++j1, ++j2);
    }
    int compareVersion(string version1, string version2) {
        return compareVersion(version1, version2, 0, 0);
    }
};
#endif