import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while(low <= high):
            index = int((low + high) / 2)
            left, mid, right = -math.inf, nums[index], -math.inf
            if index != 0:
                left = nums[index - 1]
            if index != len(nums) - 1:
                right = nums[index + 1]
            if mid > left and mid > right:
                return index
            else:
                if left < mid:
                    low = index + 1
                else:
                    high = index
