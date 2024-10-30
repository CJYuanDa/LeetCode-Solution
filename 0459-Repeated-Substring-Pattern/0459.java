class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();

        for (int i = 1; i < (n / 2) + 1; i++) {
            if (n % i == 0) {
                String sub = s.substring(0, i);

                StringBuilder repeat = new StringBuilder();
                int count = n / i;

                for (int j = 0; j < count; j++) {
                    repeat.append(sub);
                }

                if (repeat.toString().equals(s))
                    return true;
            }
        }

        return false;
    }

    public boolean repeatedSubstringPattern1(String s) {
        String doubleS = s + s;
        String newS = doubleS.substring(1, doubleS.length() - 1);

        return newS.contains(s);
    }
}