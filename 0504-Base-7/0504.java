class Solution {
    public String convertToBase7(int num) {
        if (num == 0)
            return "0";

        String ans = "";
        boolean isPositive = num > 0;
        int newNum = Math.abs(num);

        while (newNum > 0) {
            ans = Integer.toString(newNum % 7) + ans;
            newNum /= 7;
        }

        return isPositive ? ans : "-" + ans;
    }

    public String convertToBase7(int num) {
        return Integer.toString(num, 7);
    }
}