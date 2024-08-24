class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        L = 0 
        R = len(s) - 1

        while L < R:
            if s[L] in vowels and s[R] in vowels:
                temp = s[R]
                s[R] = s[L]
                s[L] = temp
                L += 1
                R -= 1
                continue
            
            if s[L] not in vowels:
                L += 1
            
            if s[R] not in vowels:
                R -= 1
        
        return "".join(s)