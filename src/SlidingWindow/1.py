""""

a a d a d c a d c

все неповторяющиеся тройки

проверка дубликатов:
добавим state - таблицу в которую добавляем значения и колчисетво

"""
import collections


class Solution:
    def countGoodSubStrings(self, s: str) -> int:
        memory, left, res = collections.defaultdict(int), 0, 0
        print(memory)

        for right, cur_char in enumerate(s):
            memory[cur_char] += 1

            if right - left == 3:
                # если размер окна больше чем 3 (4)
                left_char = s[left] #берем левый символ
                memory[left_char] -= 1 #уменьшаем количество у левого символа

                if memory[left_char] == 0: del memory[left_char] #удаляем символ если его количество 0

                left += 1 #двигаем левую границу

            #после этого размер окна стал 3 и если количество элементов в таблице 3
            #то увеличиваем результат
            if len(memory) == 3:
                res += 1

        return res
