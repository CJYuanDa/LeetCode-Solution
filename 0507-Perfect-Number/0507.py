class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        max_div = num
        div = 2
        sum_div = 1

        while div < max_div:
            if num % div == 0:
                relative_div = num // div
                sum_div = sum_div + div + relative_div
                max_div = relative_div
            
            if sum_div > num:
                return False
                
            div += 1
        
        return num == sum_div


    def checkPerfectNumber1(self, num: int) -> bool:
        if num <= 1:
            return False
        
        sum_div = 1
        div = 2

        # Iterate only until the square root of num
        while div * div <= num:
            if num % div == 0:
                sum_div += div
            
            if div != num // div: # Avoid adding the square root twice
                sum_div += num // div 
            
            div += 1
        
        return sum_div == num
