# Link: https://leetcode.com/problems/n-th-tribonacci-number

class Solution {
    public int tribonacci(int n) {
        if (n == 0) {
            return 0;
        }
        else if (n == 1 || n == 2) {
            return 1;
        }
        else {
            int mem = 0;
            int mem2 = 1;
            int mem3 = 1;

            int res = 0;
            int i;
            for (i = 0; i < n-2; i++) {
                res = mem + mem2 + mem3;
                mem = mem2;
                mem2 = mem3;
                mem3 = res;
            }
            return res;
        }
    }
}
