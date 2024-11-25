class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_cap = 0

        for letter in word:
            if ord(letter) >= 65 and ord(letter) <= 90:
                count_cap += 1
        
        if count_cap == len(word):
            return True
        if count_cap == 0:
            return True
        if count_cap == 1 and ord(word[0]) <= 90:
            return True

        return False
    
    def detectCapitalUse1(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1::].islower():
            return True
        return False