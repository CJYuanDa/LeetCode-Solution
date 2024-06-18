import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            // if value of (target - nums[i]) in the HashMap Key
            if (hash.containsKey(target - nums[i])) {
                int[] answer = { hash.get(target - nums[i]), i };
                return answer;
            }
            hash.put(nums[i], i);
        }

        return null;
    }
}