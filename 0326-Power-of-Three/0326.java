class Solution {
    public boolean isPowerOfThree(int n) {
        int maxN = (int) Math.pow(3, 19);

        return n > 0 && maxN % n == 0;
    }
}