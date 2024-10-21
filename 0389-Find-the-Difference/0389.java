class Solution {
    public char findTheDifference(String s, String t) {
        int[] count = new int[26];

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        for (char c : sArray) {
            count[c - 'a']++;
        }

        for (char c : tArray) {
            count[c - 'a']--;
            if (count[c - 'a'] < 0)
                return c;
        }

        return 'a';
    }
}