class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        border = 1
        while border ** 2 < num:
            border += 1
        
        area = border ** 2

        return area == num

    def isPerfectSquare1(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
            
        return False