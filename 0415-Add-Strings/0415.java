class Solution {
    public String addStrings(String num1, String num2) {
        int index1 = num1.length() - 1, index2 = num2.length() - 1;
        int carry = 0;
        String ans = "";

        while (index1 >= 0 || index2 >= 0) {
            int x = 0, y = 0;
            if (index1 >= 0) {
                x = num1.charAt(index1) - 48;
                index1--;
            }
            if (index2 >= 0) {
                y = num2.charAt(index2) - 48;
                index2--;
            }

            int add = x + y + carry;
            System.out.println(add);
            if (add >= 10) {
                carry = 1;
                ans = String.valueOf(add % 10) + ans;
            } else {
                ans = String.valueOf(add) + ans;
                carry = 0;
            }
        }

        if (carry == 1) {
            ans = "1" + ans;
        }

        return ans;

    }
}