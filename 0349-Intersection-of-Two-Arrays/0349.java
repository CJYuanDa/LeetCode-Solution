import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> res = new ArrayList<>();

        for (int num : nums1) {
            if (contain(nums2, num) && !res.contains(num)) {
                res.add(num);
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();

    }

    public boolean contain(int[] nums, int checkNum) {
        for (int num : nums) {
            if (num == checkNum)
                return true;
        }
        return false;
    }

    public int[] intersection1(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int num : nums1) {
            set1.add(num);
        }

        // find the intersection store in set2
        for (int num : nums2) {
            if (set1.contains(num))
                set2.add(num);
        }

        int[] res = new int[set2.size()];
        int index = 0;
        for (int num : set2) {
            res[index] = num;
            index++;
        }

        return res;
    }
}