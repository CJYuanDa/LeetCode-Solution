import java.util.ArrayList;

class Solution {
    public boolean isPalindrome(String s) {
        ArrayList<Character> charArr = new ArrayList<>();
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // conver to ascII code
            if (((int) c > 96 && (int) c < 123) || ((int) c > 47 && (int) c < 58)) {
                charArr.add(c);
            }
        }

        int left = 0;
        int right = charArr.size() - 1;

        while (left < right) {
            if (charArr.get(left) != charArr.get(right))
                return false;
            left++;
            right--;
        }

        return true;
    }
}