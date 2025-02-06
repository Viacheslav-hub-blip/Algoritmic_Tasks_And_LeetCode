class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSub = ''
        if len(s) == 1:
            return s
        if len(s) == 2 and (s != s[::-1]):
            return s[0]
        for index in range(len(s) - 1):
            current_sub = s[index]
            for nex_index in range(index + 1, len(s)):

                current_sub += s[nex_index]
                print(current_sub)
                if current_sub == current_sub[::-1]:

                    if len(current_sub) > len(longestSub):
                        longestSub = current_sub

        return longestSub


s = Solution()
print(s.longestPalindrome('ac'))
