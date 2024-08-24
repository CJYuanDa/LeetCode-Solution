import java.util.ArrayList;
import java.util.List;

class Solution {
    public String reverseVowels(String s) {
        List<Character> vowels = new ArrayList<>(List.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        char[] sArray = s.toCharArray();
        int left = 0, right = sArray.length - 1;

        while (left < right) {
            if (vowels.contains(sArray[left]) && vowels.contains(sArray[right])) {
                char temp = sArray[right];
                sArray[right] = sArray[left];
                sArray[left] = temp;
                right++;
                left--;
                continue;
            }

            if (!vowels.contains(sArray[left]))
                left++;
            if (!vowels.contains(sArray[right]))
                right++;
        }

        return String.valueOf(sArray);
    }
}