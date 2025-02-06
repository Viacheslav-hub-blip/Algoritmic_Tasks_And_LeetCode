from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        new_num = sorted(nums1 + nums2)
        len_num  = len(new_num)

        if len_num == 0:
            return 0.0
        if len_num % 2 != 0:
            return float(new_num[len_num//2])
        else:

            av = (new_num[len_num//2 -1] +  new_num[len_num//2]) / 2
            return av


s  = Solution()
print(s.findMedianSortedArrays([1,2], [3, 4]))
