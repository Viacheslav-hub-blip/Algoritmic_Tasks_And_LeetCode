from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> [[int]]:
        result  = []
        nums.sort()

        for i, element in enumerate(nums):
            if i and element == nums[i -1]:
                continue

            left = i+ 1
            right  = len(nums) - 1

            while left < right:
                three_sum  = element + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([element, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
