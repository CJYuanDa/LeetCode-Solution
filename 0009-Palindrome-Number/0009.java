class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;

        int div = 1;
        // div * 10 may > 2^31 - 1
        while (x >= (long) div * 10) {
            div *= 10;
        }

        while (x > 0) {
            int right = x % 10;
            int left = x / div;

            if (left != right)
                return false;

            x = (x % div) / 10;
            div /= 100;
        }

        return true;
    }

    public boolean isPalindrome1(int x) {
        if (x < 0)
            return false;

        int reverse = 0, n = x;

        while (n > 0) {
            int digit = n % 10;
            reverse = reverse * 10 + digit;
            n /= 10;
        }

        return x == reverse;
    }
}