import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int singleNumber(int[] nums) {
        List<Integer> numList = Arrays.stream(nums).boxed().collect(Collectors.toList());

        for (int num : nums) {
            int num1 = numList.indexOf(num);
            int num2 = numList.lastIndexOf(num);
            if (num1 == num2)
                return num;
        }
        return -1;
    }
}