class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        boolean oddFound = false;
        int ans = 0;

        for (int count : counter.values()) {
            if (count % 2 == 0) {
                ans += count;
            } else {
                ans += count - 1;
                oddFound = true;
            }
        }

        if (oddFound) {
            ans += 1;
        }

        return ans;
    }
}