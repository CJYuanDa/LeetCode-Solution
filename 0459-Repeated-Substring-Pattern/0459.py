class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Try each possible substring length
        for len_sub in range(1, n // 2 + 1):
            # Check if n is divisible by len_sub
            if n % len_sub == 0:
                # Extract the substring and repeat it to match s
                sub = s[:len_sub]
                repeat = sub * (n // len_sub)

                # Check if this repeated string equals s
                if repeat == s:
                    return True
        
        return False
    
    def repeatedSubstringPattern1(self, s: str) -> bool:
        new_s = (s + s)[1:-1]
        return s in new_s