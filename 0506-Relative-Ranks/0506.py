from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_sort = sorted(score, reverse=True)
        ans = []

        for rank in score:
            place = rank_sort.index(rank)
            if place == 0:
                ans.append('Gold Medal')
            elif place == 1:
                ans.append('Silver Medal')
            elif place == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(place + 1))
        

        return ans