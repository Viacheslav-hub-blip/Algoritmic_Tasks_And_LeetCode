class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < -2**31:
            return False
        elif x > 2**31-1:
            return False

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

s  = Solution()
print(s.isPalindrome(-4**31))