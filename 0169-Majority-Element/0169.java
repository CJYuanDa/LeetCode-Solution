import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();

        for (int num : nums) {
            if (hash.containsKey(num)) {
                hash.put(num, hash.get(num) + 1);
            } else {
                hash.put(num, 1);
            }

            if (hash.get(num) > nums.length / 2) {
                return num;
            }
        }

        return -1;
    }
}