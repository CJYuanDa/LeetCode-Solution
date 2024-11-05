class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ans = 0, count = 0;

        for (int num : nums) {
            if (num == 0) {
                count = 0;
            } else {
                count++;
            }

            if (count > ans)
                ans = count;
        }

        return ans;
    }
}