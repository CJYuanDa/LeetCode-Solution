class Solution {
    public String toHex(int num) {
        if (num == 0)
            return "0";

        char[] hexa = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };
        String ans = "";

        while (num != 0) {
            // num & 15 extracts the last 4 bits (equivalent to num % 16)
            ans = hexa[num & 15] + ans;

            // Unsigned right shift by 4 bits (fills in 0 for negative numbers)
            num >>>= 4;
        }

        return ans;
    }
}