class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        # x = first preceding number, y = second preceding number
        x, y = 0, 1
        ans = 0

        for i in range(n - 1):
            ans = x + y
            x = y
            y = ans
        
        return ans
        