class Solution:
    def toHex(self, num: int) -> str:
        hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ans = ""

        if num > 0:
            while num > 0:
                ans = hexa[num % 16] + ans
                num = num // 16
            
            return ans
        elif num < 0:
            for i in range(8):
                ans = hexa[num % 16] + ans
                num = num // 16

            return ans
        else:
            return "0"
