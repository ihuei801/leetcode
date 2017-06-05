void printNum(vector<char> &num)
{
    int start = 0;
    for (int i = 0; i < num.size(); i++)
    {
        if (!start && num[i] != '0')
            start = 1;
        if (start)
            printf("%c", num[i]);
    }
    printf("\n");
}

void genNum(vector<char> &num, int index, int n)
{
    for (int i = 0; i < 10; i++)
    {
        num[index] = i + '0';
        if (index == n-1)
            printNum(num);
        else
            genNum(num, index+1, n);
    }
}

int main(int argc, const char * argv[])
{
    int n = 3;
    vector<char> num(n, '0');
    genNum(num, 0, n);
}
