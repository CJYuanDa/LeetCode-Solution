class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        #  n steps = (n - 2) steps + (n - 1) steps
        oneStep = 1
        twoSteps = 2
        for i in range(n - 2):
            currentWay = oneStep + twoSteps
            oneStep = twoSteps
            twoSteps = currentWay
        
        return twoSteps