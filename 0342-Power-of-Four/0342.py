class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 0x55555555: 01010101010101010101010101010101
        # 2:                                        10
        # 4:                                       100
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0