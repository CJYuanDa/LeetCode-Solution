from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for i in range(1, numRows):
            previous = triangle[i - 1]
            current = [1]

            for j in range(1, i):
                current.append(previous[j - 1] + previous[j])
            
            current.append(1)
        
            triangle.append(current)

        return triangle