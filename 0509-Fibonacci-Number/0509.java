class Solution {
    public int fib(int n) {
        if (n <= 1)
            return n;
        int x = 0, y = 1, ans = 0;

        for (int i = 0; i < n - 1; i++) {
            ans = x + y;
            x = y;
            y = ans;
        }

        return ans;
    }
}