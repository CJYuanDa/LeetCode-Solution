class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        ans = ""

        carry = 0
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0 and index2 >= 0:
                add = int(num1[index1]) + int(num2[index2]) + carry
            elif index1 >= 0:
                add = int(num1[index1]) + carry
            elif index2 >= 0:
                add = int(num2[index2]) + carry

            if add >= 10:
                carry = 1
                add %= 10
                ans = str(add) + ans
            else:
                ans = str(add) + ans
                carry = 0

            index1 -= 1
            index2 -= 1
        
        if carry != 0:
            ans = "1" + ans

        return ans

        