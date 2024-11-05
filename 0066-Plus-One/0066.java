class Solution {
    public int[] plusOne(int[] digits) {
        int idx = digits.length - 1;

        // iterate from right to left
        for (int i = idx; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // [9, 9, 9] -> [0, 0, 0, 0]
        digits = new int[digits.length + 1];

        // [0, 0, 0, 0] -> [1, 0, 0, 0]
        digits[0] = 1;
        return digits;
    }
}