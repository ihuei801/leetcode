void partition(vector<int> &data, int start, int end)
{
    int mid = (start + end) >> 1;
    swap(&data[mid], &data[end]);

    int small = start - 1;
    for (int i = start; i < end; i++)
    {
        if (data[i] < data[end])
        {
            small++;
            if (small != i)
            {
                swap(&data[small], &data[i]);
            }
        }
    }

    small++;
    swap(&data[small], &data[end]);
}
