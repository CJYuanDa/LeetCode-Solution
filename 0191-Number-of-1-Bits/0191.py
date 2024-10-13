class Solution:
    def hammingWeight(self, n: int) -> int:
        # change the n to binary, the type of bit is string
        bit = bin(n)
        return bit.count("1")