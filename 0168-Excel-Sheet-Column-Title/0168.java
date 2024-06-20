class Solution {
    public String convertToTitle(int columnNumber) {
        String ans = "";
        while (columnNumber > 0) {
            // A -> 1
            columnNumber--;
            // get the ascII number convert to character
            ans = Character.toString(columnNumber % 26 + 65) + ans;
            columnNumber /= 26;
        }
        return ans;
    }
}