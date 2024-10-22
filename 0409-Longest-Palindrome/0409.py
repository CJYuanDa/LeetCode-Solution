from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = Counter(s)
        found_odd = False
        ans = 0

        for c, count in map.items():
            # Add even counts entirely
            if count % 2 == 0:
                ans += count
            else:
                ans += count - 1 # Add the largest even part
                found_odd = True 
        
        # Add one more character for the center if an odd frequency is found
        if found_odd:
            ans += 1
    
        return ans