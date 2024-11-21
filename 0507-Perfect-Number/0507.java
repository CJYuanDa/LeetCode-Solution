class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num <= 1)
            return false;

        int sum_div = 1, div = 2;

        while (div * div <= num) {
            if (num % div == 0) {
                sum_div += div;

                if (div != num / div) {
                    sum_div += num / div;
                }
            }

            div++;
        }

        return sum_div == num;
    }
}