class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLen = 0

        for index in range(len(s)):
            current_sub = s[index]
            maxLen=max(len(current_sub), maxLen)
            print('start sub', current_sub)
            for next_index in range(index + 1, len(s)):
                if s[next_index] in current_sub:
                    break
                else:
                    current_sub += s[next_index]
                    maxLen = max(len(current_sub), maxLen)
                    print(current_sub)

        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring(""))