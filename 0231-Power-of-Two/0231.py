class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False

        while n > 2:
            if n % 2 != 0: return False
            n = n // 2
        return True
    
    def isPowerOfTwo1(self, n: int) -> bool:
        # &, |, ^ are bitwise operators
        # compare every digit of two binary numbers
        # & (and): 0, 0 -> 0; 1, 0 -> 0; 1, 1 -> 1
        # |  (or): 0, 0 -> 0; 1, 0 -> 1; 1, 1 -> 1

        # 8 = 1000
        # 7 = 0111
        # 8 & 7 = 0000
        return n > 0 and (n & (n - 1)) == 0
    
    def isPowerOfTwo2(self, n: int) -> bool:
        max_n = 2 ** 30
        return n > 0 and max_n % n == 0