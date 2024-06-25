class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert binary number (string) to decimal number (int)
        a = int(a, 2)
        b = int(b, 2)

        # convert decimal numbet into binary number
        # the output is string, which would start with the prefix "0b" ...
        return bin(a + b)[2:]