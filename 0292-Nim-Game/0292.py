class Solution:
    def canWinNim(self, n: int) -> bool:
        # lose: 4 
        # win: 1 2 3 5 6 7 9 10 11 12 13
        return n % 4 != 0
        