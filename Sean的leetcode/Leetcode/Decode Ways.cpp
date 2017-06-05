/*Dynamic programming: if s[i] is valid, f(i) += f(i-1)
                       if (s[i-1], s[i]) pair is valid, f(i) += f(i-2)
*/                       
class Solution {
public:

    int check(char c)
    {
        return (c != '0') ? (1) : (0);
    }
    
    int check(char first, char sec)
    {
        if (first == '1' || (first == '2' && '0' <= sec && sec <= '6'))
            return 1;
        else
            return 0;
    }
    
    int numDecodings(string s) {
    
        
        int len = s.size();
        if (len == 0) return 0;
        if (len == 1) return check(s[0]);

        int fn, fn_1, fn_2;
        fn_1 = check(s[0]); // f(n-1) == f(1)
        fn_2 = 1;           // f(n-2) == f(0)
        
        for (int i = 1; i < len; i++)
        {
            fn = 0; 
            
            if (check(s[i]))
                fn += fn_1;
            if (check(s[i-1], s[i]))
                fn += fn_2;
                
            if (fn == 0)                
                break;
                
            fn_2 = fn_1;
            fn_1 = fn;
        }
        return fn;
    }
};