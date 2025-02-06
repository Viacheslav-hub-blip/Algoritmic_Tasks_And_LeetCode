from typing import List
from itertools import permutations


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        letter_map = {'2': 'abc',
                      '3': 'def',
                      '4': 'ghi',
                      '5': 'jkl',
                      '6': 'mno',
                      '7': 'pqrs',
                      '8': 'tuv',
                      '9': 'wxyz'
                      }

        ans, sol = [], []

        n = len(digits)

        def backtrack(i=0):
            print('i', i)
            if i == n:
                ans.append(''.join(sol))
                return

            for letter in letter_map[digits[i]]:
                print('let', letter, 'sol', sol)
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()
                print('sol2', sol)

        backtrack(0)
        return ans


s = Solution()
print(s.letterCombinations('23'))
