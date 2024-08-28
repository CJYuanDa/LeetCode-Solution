from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j, content = 0, 0, 0
        g = sorted(g)
        s = sorted(s)

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return content