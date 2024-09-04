class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 0

        while 3 ** power < n:
            power += 1
        
        return 3 ** power == n

    def isPowerOfThree1(self, n: int) -> bool:
        max_n = 3 ** 19

        return n > 0 and max_n % n == 0


