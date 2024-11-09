class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: 
            return '0'

        ans = ""

        is_negative = num < 0
        new_num = abs(num)

        while new_num > 0:
            ans = str(new_num % 7)+ ans
            new_num //= 7
        
        return ans if not is_negative else '-' + ans