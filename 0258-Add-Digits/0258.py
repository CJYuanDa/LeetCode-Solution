class Solution:
    def addDigits(self, num: int) -> int:
        res = self.sum_digits(num)
        
        while res % 10 != res:
            res = self.sum_digits(res)

        return res
    
    def sum_digits(self, num: int) -> int:
        output = 0
        while num > 0:
            output += num % 10
            num = num // 10
        return output


class Solution1:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9