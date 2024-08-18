class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern = {}
        map_s = {}
        list_s = s.split()

        if len(pattern) != len(list_s):
            return False
        
        for index, char in enumerate(pattern):
            word = list_s[index]

            if char in map_pattern and map_pattern[char] != word:
                return False

            if word in map_s and map_s[word] != char:
                return False
            
            map_pattern[char] = word
            map_s[word] = char
            
        
        return True