class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        //note: we should compare "min(C, G) > max(A, E)" first.
        //Otherwise, min(C, G) - max(A, E) may cause INT overflow.
        int share_x = min(C, G) > max(A, E) ? min(C, G) - max(A, E) : 0;
        int share_y = min(D, H) > max(B, F) ? min(D, H) - max(B, F) : 0;

        return (G - E) * (H - F) + (C - A) * (D - B) - share_x * share_y;
    }
};