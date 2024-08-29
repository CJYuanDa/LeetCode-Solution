class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        div = 1
        # if x = 1234, div = 1000
        while x >= div * 10:
            div *= 10
        
        while x > 0:
            right = x % 10
            left = x // div

            if right != left: return False

            # 1234 -> 234 -> 23
            x = (x % div) // 10
            # 1000 -> 10, because I got rid off 2 digits
            div /= 100
        
        return True
    
    def isPalindrome1(self, x: int) -> bool:
        if x < 0: return False
        
        n = x
        reverse = 0
        
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10
        
        return x == reverse