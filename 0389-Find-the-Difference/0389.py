class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t

        s_map = {}
        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        
        for c in t:
            if c not in s_map or s_map[c] == 0:
                return c
            s_map[c] -= 1
    
    def findTheDifference1(self, s: str, t: str) -> str:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            index = ord(c) - ord('a')
            count[index] -= 1

            if count[index] < 0:
                return count[index]

