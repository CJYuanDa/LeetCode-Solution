class Solution {
    public String licenseKeyFormatting(String s, int k) {
        char[] arrayS = s.toCharArray();
        int index = arrayS.length - 1;
        int count = 0;
        String ans = "";

        while (index >= 0) {
            if (arrayS[index] == '-') {
                index--;
                continue;
            }

            if (count == k) {
                ans = '-' + ans;
                count = 0;
            }

            ans = Character.toUpperCase(arrayS[index]) + ans;
            count++;
            index--;
        }

        return ans;
    }
}