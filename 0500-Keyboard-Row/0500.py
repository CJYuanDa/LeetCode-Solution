from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the keyboard rows as sets for faster lookup
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []
        for word in words:
            # Convert the word to lowercase for uniformity
            lower_word = set(word.lower())
            
            # Check if the entire word is in one of the rows
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(word)

        return result