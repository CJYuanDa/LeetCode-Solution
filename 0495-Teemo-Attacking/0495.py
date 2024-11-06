from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0

        # [1,2,3,4,6,10] duration = 2 
        #  1 1 1 2 2  2

        for i in range(len(timeSeries) - 1):
            pois = min(duration, timeSeries[i + 1] - timeSeries[i])
            total += pois
        
        return total + duration