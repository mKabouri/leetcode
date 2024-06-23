// Link: https://leetcode.com/problems/climbing-stairs/

class Solution {
    public int climbStairs(int n) {
        if (n == 1 || n == 2) {
            return n;
        }
        else {
            int res = 0;
            int save1 = 1;
            int save2 = 2;
            for (int i = 2; i < n; i++) {
                res = 0;    
                res+=save1+save2;
                save1=save2;
                save2=res;
            }
            return res;  
        }    
    }
}
