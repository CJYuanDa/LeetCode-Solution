class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        // iterate the first word in strs
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            // check every word in strs
            for (String str : strs) {
                if (str.indexOf(prefix + c) != 0) {
                    return prefix;
                }
            }
            prefix += c;
        }
        return prefix;
    }
}