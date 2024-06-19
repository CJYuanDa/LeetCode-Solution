class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_arr = []
        s = s.lower()
        for char in s:
            # to check is Alphanumeric characters or not
            if char.isalnum():
                str_arr.append(char)
        
        # index from the left
        left = 0
        # index from the right
        right = len(str_arr) - 1
        while left < right:
            if str_arr[left] != str_arr[right]:
                return False
            left += 1
            right -= 1
        return True