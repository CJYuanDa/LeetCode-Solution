import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> visit = new HashSet<>();

        while (!visit.contains(n)) {
            visit.add(n);

            n = sumOfSquare(n);

            if (n == 1)
                return true;
        }
        return false;
    }

    public int sumOfSquare(int n) {
        int output = 0;

        while (n > 0) {
            int digit = n % 10;
            output += Math.pow(digit, 2);
            n /= 10;
        }

        return output;
    }
}