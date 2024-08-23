class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1

        while L < R:
            temp = s[R]
            s[R] = s[L]
            s[L] = temp
            L += 1
            R -= 1