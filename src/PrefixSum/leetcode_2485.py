class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers_list = [x for x in range(1, n + 1)]
        prefix_sum = [0]
        for i in range(1, n + 1):
            prefix_sum.append(prefix_sum[i - 1] + numbers_list[i - 1])

        for x in range(len(numbers_list)):
            prefix_sum_before_x = prefix_sum[x + 1]
            prefix_sum_after_x = prefix_sum[-1] - prefix_sum[x]

            if prefix_sum_before_x == prefix_sum_after_x:
                return numbers_list[x]
        return -1


sol = Solution()
print(sol.pivotInteger(2))
