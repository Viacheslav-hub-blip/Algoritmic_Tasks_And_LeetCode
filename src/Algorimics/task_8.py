class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        symbs  = 'qwertyuiopasdfghjklzxcvbnm'
        minus = False
        current_sub = ""

        if len(s) == 0:
            return 0
        list_s  = list(s)

        for sym in range(len(list_s)):
            if (list_s[sym] in numbers) or (list_s[sym]  in ['+', '-']):
               break
            elif list_s[sym] in symbs:
                return 0
            else:
                list_s[sym] = '*'

        s  = ''.join(list_s)

        s  = s.replace('*', '')



        if len(s) == 0:
            return 0

        if s[0] == "-":
            minus = True
        elif s[0] == '+':
            pass
        elif s[0] not in numbers:
            return 0

        for current_sym in range(len(s)):
            if s[current_sym] in numbers:
                current_sub += s[current_sym]
            elif (current_sym == 0 and minus) or (current_sym == 0 and s[current_sym] == '+'):
                pass
            else:
                break

        if current_sub == '':
            return 0

        if minus:
            res = -int(current_sub)
        else:
            res = int(current_sub)

        if res < -2 ** 31:
            res = -2 ** 31
        elif res > 2 ** 31 - 1:
            res = 2 ** 31 -1

        return res


s = Solution()
print(s.myAtoi("589275982728572"))
