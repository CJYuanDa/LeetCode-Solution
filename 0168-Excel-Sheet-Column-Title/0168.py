class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            # A -> 1
            columnNumber -= 1
            # get the ascII number convert to character
            ans = chr(columnNumber % 26 + 65) + ans
            # only get Quotient (28 / 26 = 1 ... 2, 1 is Quotent)
            columnNumber //= 26

        return ans