import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> hash = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for (int num : nums1) {
            hash.put(num, hash.getOrDefault(num, 0) + 1);
        }

        for (int num : nums2) {
            if (hash.containsKey(num) && hash.get(num) > 0) {
                res.add(num);
                hash.put(num, hash.get(num) - 1);
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }

    public int[] intersect1(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        List<Integer> res = new ArrayList<>();
        int i = 0, j = 0;

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                res.add(nums1[i]);
                i++;
                j++;
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}