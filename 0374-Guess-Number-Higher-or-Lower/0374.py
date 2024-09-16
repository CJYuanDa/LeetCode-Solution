# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n
        while L <= R:
            M = L + (R - L) // 2

            if guess(M) == -1: # type: ignore
                R = M - 1
            elif guess(M) == 1: # type: ignore
                L = M + 1
            else:
                return M