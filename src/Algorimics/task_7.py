class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            rev_int  = -int(str(x)[1:][::-1])
        else:
            rev_int = int(str(x)[::-1])

        return rev_int

s  = Solution()
print(s.reverse(120))