from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # create all 0's array [0, 0, 0, 0 ,0]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # if i is 5: 5 -> 101, so 5 >> 1 = 3 (10) + the last one bit (i & 1)
            # take the previous result and + (i & 1)
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp