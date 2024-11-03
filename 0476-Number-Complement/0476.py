class Solution:
    def findComplement(self, num: int) -> int:
        bit = list(bin(num)[2:])

        for i in range(len(bit)):
            if bit[i] == '0':
                bit[i] = '1'
            else:
                bit[i] = '0'
        
        return int(''.join(bit), 2)
    
    def findComplement1(self, num: int) -> int:
        # Find the bit length of the number
        bit_length = len(bin(num)[2:])

        # Create a bitmask with all bits set to 1 of the same length as num
        mask = (1 << bit_length) - 1

        return num ^ mask