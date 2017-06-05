#if 0 //O(n) solution
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int sum = 0;
        for (int i = 31; i >= 0; i--)
        {
            sum |= (n & 1) << i;
            n >>= 1;
        }
        return sum;
    }
};
#else //O(logn) solution
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16 & (int)0x0000FFFF) | (n << 16 & (int)0xFFFF0000);
        n = (n >> 8 & (int)0x00FF00FF) | (n << 8 & (int)0xFF00FF00);
        n = (n >> 4 & (int)0x0F0F0F0F) | (n << 4 & (int)0xF0F0F0F0);
        n = (n >> 2 & (int)0x33333333) | (n << 2 & (int)0xCCCCCCCC);
        return (n >> 1 & (int)0x55555555) | (n << 1 & (int)0xAAAAAAAA);
    }
};
#endif