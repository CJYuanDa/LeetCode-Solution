import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map1 = new HashMap<>();
        for (int i = 0; i < nums1.length; i++) {
            map1.put(nums1[i], i);
        }

        int[] ans = new int[nums1.length];
        Arrays.fill(ans, -1);

        Stack<Integer> stack = new Stack<>();

        for (int num : nums2) {

            while (!stack.empty() && num > stack.peek()) {
                int index = map1.get(stack.pop());
                ans[index] = num;
            }

            if (map1.containsKey(num)) {
                stack.push(num);
            }
        }

        return ans;
    }
}