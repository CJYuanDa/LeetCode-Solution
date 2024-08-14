class Solution {
    public void moveZeroes(int[] nums) {
        int zero = 0;

        for (int noneZero = 0; noneZero < nums.length; noneZero++) {
            if (nums[noneZero] != 0) {
                int swap = nums[zero];
                nums[zero] = nums[noneZero];
                nums[noneZero] = swap;
                zero++;
            }
        }

    }
}