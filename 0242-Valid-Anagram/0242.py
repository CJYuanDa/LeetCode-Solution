class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # key, value = char, times
        map = {}

        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        for char, times in map.items():
            if t.count(char) != times:
                return False
        
        return True
    
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)