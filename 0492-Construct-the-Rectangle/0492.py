import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        SQRT = math.floor(math.sqrt(area))
        L, W = SQRT, SQRT

        if L * W == area: return [L, W]
     
        while L * W != area:
            if L * W < area:
                L += 1
            elif L * W > area:
                W -= 1
        return [L, W]

    def constructRectangle1(self, area: int) -> List[int]:
        W = math.floor(math.sqrt(area))  # Start from the square root
        while area % W != 0:  # Find a W that divides the area evenly
            W -= 1
        L = area // W  # Calculate L directly
        return [L, W]