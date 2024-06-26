class Solution:
    def romanToInt(self, s: str) -> int:
        # last index
        idx = len(s) - 1

        # answer
        result = 0

        # iterate the string from right to left
        while idx >= 0:
            if s[idx] == 'I':
                # IV -> 4, IX -> 9
                if idx < len(s) - 1 and (s[idx + 1] == 'V' or s[idx + 1] == 'X'):
                    result -= 1
                else:
                    result += 1
            elif s[idx] == 'V':
                result += 5
            elif s[idx] == 'X':
                # XL -> 40, XC -> 90
                if idx < len(s) - 1 and (s[idx + 1] == 'L' or s[idx + 1] == 'C'):
                    result -= 10
                else:
                    result += 10
            elif s[idx] == 'L':
                result += 50
            elif s[idx] == 'C':
                # CD -> 500, CM -> 900
                if idx < len(s) - 1 and (s[idx + 1] == 'D' or s[idx + 1] == 'M'):
                    result -= 100
                else: 
                    result += 100
            elif s[idx] == 'D':
                result += 500
            elif s[idx] == 'M':
                result += 1000
            idx -= 1

        return result
