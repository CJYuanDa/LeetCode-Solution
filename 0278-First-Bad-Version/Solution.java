/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int L = 1, R = n, res = 1;

        while (L <= R) {
            int M = L + (R - L) / 2;
            if (isBadVersion(M)) {
                res = M;
                R = M - 1;
            } else {
                L = M + 1;
            }
        }

        return res;
    }
}