class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0

        while index_s < len(s):
            # has checked all character of t
            if index_t > len(t) - 1:
                return False
            
            # if match, increase both index
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            # if not match, increase index of t
            else:
                index_t += 1
        
        return True