from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        current = ''
        
        for symb_in_first in range(len(strs[0])):
            print(symb_in_first)

s  = Solution()
print(s.longestCommonPrefix(['ddqdqdq']))