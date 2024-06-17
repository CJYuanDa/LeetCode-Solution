class Solution {
    public int climbStairs(int n) {
        // n steps = (n - 2) steps + (n - 1) steps
        int oneStep = 1;
        int twoSteps = 2;
        if (n < 3)
            return n;
        for (int i = 3; i <= n; i++) {
            int currentWay = oneStep + twoSteps;
            oneStep = twoSteps;
            twoSteps = currentWay;
        }
        return twoSteps;
    }
}