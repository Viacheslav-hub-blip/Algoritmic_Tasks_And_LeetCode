from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * (len(nums) + 1)
        reversed_prefix_sum=[0] * (len(nums) + 1)
        res = []

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            reversed_prefix_sum[-i-2] = reversed_prefix_sum[-i-1] + nums[-i-1]
        prefix_sum = prefix_sum[:len(nums)]
        reversed_prefix_sum = reversed_prefix_sum[len(reversed_prefix_sum)-len(nums):]

        for i in range(len(nums)):
            res.append(abs(reversed_prefix_sum[i] - prefix_sum[i]))
        return res

sol  = Solution()
print(sol.leftRightDifference([1]))