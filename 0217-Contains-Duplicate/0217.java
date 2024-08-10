import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> hash = new HashMap<>();

        for (int num : nums) {
            if (hash.containsKey(num))
                return true;
            hash.put(num, 1);
        }

        return false;
    }

    public boolean containsDuplicate1(int[] nums) {
        Set<Integer> set = new HashSet<>(Arrays.stream(nums).boxed().toList());
        return nums.length != set.size();
    }
}