class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: return 1
        k = 1
        coins = 1

        while coins < n:
            k += 1
            coins = k * (k + 1) // 2
        
        return k - 1

    def arrangeCoins1(self, n: int) -> int:
        L, R = 1, n
        res = 1

        while L <= R:
            M = (L + R) // 2
            coins = M * (M + 1) // 2

            # 1, 2, 3, 4, 5 

            if coins > n:
                R = M - 1
            else:
                L = M + 1
                res = M
        
        return res