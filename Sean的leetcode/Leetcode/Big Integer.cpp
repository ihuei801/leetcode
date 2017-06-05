//use vector<int> to represent big integer. INT_MAX is 10-digit (2147483648). So, one int can
//represent up to 9-digit number (999999999)

#define MAX_NUM (999999999)
vector<int> covertToBigInt(string str)
{
    vector<int>res;
    const int MAX_DIGIT = 9;
    int remain_len = str.size();
    int start_idx, end_idx = str.size()-1;

    while (remain_len > MAX_DIGIT)
    {
        start_idx = end_idx - (MAX_DIGIT - 1);
        res.push_back(atoi(str.substr(start_idx, MAX_DIGIT).c_str()));
        end_idx = start_idx - 1;
        remain_len = end_idx + 1;
    }

    if (end_idx >= 0)
        res.push_back(atoi(str.substr(0, remain_len).c_str()));

    return res;
}

void bigIntAdd(vector<int>num1, vector<int>num2)
{
    vector<int>res;
    int size1 = num1.size();
    int size2 = num2.size();
    int first_idx = 0, sec_idx = 0;
    int carry = 0;
    int sum;

    while (first_idx < size1 || sec_idx < size2)
    {
        int num_a, num_b;

        num_a = (first_idx >= size1) ? (0) : (num1[first_idx]);
        num_b = (sec_idx >= size2) ? (0) : (num2[sec_idx]);

        sum = num_a + num_b + carry;
        if (sum > MAX_NUM)
        {
            carry = 1;
            sum -= (MAX_NUM + 1);
        }
        else
            carry = 0;

        first_idx++, sec_idx++;
        res.push_back(sum);
    }

    if (carry > 0)
        res.push_back(1);

    for (int i = res.size()-1; i >= 0; i--)
    {
        char str[10];
        if (res[i] < (MAX_NUM + 1) && i != res.size()-1)
        {
            sprintf(str,"%09d", res[i]);
            printf("%s", str);
        }
        else
            printf("%d", res[i]);
    }
    printf("\n");
}

int main(int argc, const char *argv[])
{
    bigIntAdd(covertToBigInt("123456789012345678001234567"), covertToBigInt("1"));
}
