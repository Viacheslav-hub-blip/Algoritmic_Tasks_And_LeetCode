from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        all_summ  = sum(arr)
        prefix_sum = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
        print(prefix_sum)
        prefix_sum = prefix_sum[1:]
        print(prefix_sum)
        for i in range(0, len(prefix_sum)):
            if i != 0 and i % 2 == 0:
                print('i', i, prefix_sum[i])
                all_summ+=prefix_sum[i]
        print(all_summ)


sol = Solution()
sol.sumOddLengthSubarrays([1,4,2,5,3])