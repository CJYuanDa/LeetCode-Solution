from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        # iterate the first word in strs
        for char in strs[0]:
            # check every word in strs
            for i in range(1, len(strs)):
                # index will throw error if it's not exist
                if strs[i].find(answer + char) != 0:
                    return answer
            answer += char
        return answer