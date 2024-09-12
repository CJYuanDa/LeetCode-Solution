# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 1, n
        res = 1

        while L <= R:
            M = L + (R - L) // 2
            if isBadVersion(M): # type: ignore
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res