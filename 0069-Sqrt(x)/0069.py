class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left + right) // 2
            # or mid <= x / mid to to avoid potential overflow issues when x is large
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res