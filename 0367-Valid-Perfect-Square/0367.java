class Solution {
    public boolean isPerfectSquare(int num) {
        int left = 1, right = num;

        while (left <= right) {
            int mid = (left + right) / 2;
            long square = (long) mid * mid;

            if (square == num) {
                return true;
            } else if (square > num) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return false;
    }
}