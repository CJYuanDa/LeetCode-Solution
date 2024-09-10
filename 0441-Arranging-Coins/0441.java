class Solution {
    public int arrangeCoins(int n) {
        int L = 1, R = n, res = 1;
        while (L <= R) {
            // (L + R) may > 2^31 - 1
            int M = L + (R - L) / 2; // to prevent overflow
            long coins = (long) M * (M + 1) / 2;

            if (coins > n) {
                R = M - 1;
            } else {
                L = M + 1;
                res = M;
            }
        }
        return res;
    }
}