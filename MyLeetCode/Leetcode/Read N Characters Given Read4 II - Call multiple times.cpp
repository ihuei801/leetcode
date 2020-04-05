/* buf: destination for copy
 * 
 */
// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int cnt = 0;
        while (cnt < n) {
            if (buffptr == 0) {
                buffcnt = read4(buff);
            }
            while (cnt < n && buffptr < buffcnt) {
                buf[cnt++] = buff[buffptr++];
            }
            if (buffptr == buffcnt) {
                buffptr = 0;
            }
            if (buffcnt < 4) break;
        }
        return cnt;
        
    }
    int buffptr = 0;
    int buffcnt = 0;
    char buff[4];
};