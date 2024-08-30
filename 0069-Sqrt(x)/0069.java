class Solution {
    public int mySqrt(int x) {
        if (x < 2)
            return x;
        int left = 0, right = x, res = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (mid <= x / mid) {
                res = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}