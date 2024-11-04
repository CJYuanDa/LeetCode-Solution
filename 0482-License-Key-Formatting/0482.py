class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        index = len(s) - 1
        count = 0
        ans = ''

        while index >= 0:
            if s[index] == '-':
                index -= 1
                continue

            if count == k:
                ans = '-' + ans
                count = 0

            ans = s[index].upper() + ans
            count += 1

            index -= 1
        
        return ans