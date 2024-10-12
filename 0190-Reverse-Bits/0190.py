class Solution:
    def reverseBits(self, n: int) -> int:
        
        # 1. set the result = 0
        # 2. iterate the 0 to 31, because n is 32 bits integer
        # 3. reverse the bit
        # 4. get the bit from the right to left
        # 5. put the bit from the left to right

        res = 0 # 1
        
        for i in range(32): # 2
            # use & to get the bit number
            bit = (n >> i) & 1 # 4
            # use | to put the bit number 
            res = res | (bit << (31 - i)) # 5

        return res