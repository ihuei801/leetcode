// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer not the place of file
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int count = 0;
        while (count < n)
        {
            int r = read4(buf);
            count += r;
            buf += r;
            if (r < 4)
                break;
        }
        int len = min(count, n);
        return len;
    }
};