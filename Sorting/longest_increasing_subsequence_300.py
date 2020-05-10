import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        memo = [nums[0]]
        for num in nums[1:]:
            i = bisect.bisect_left(memo, num)
            if i == len(memo):
                memo.append(num)
            else:
                memo[i] = num
        return len(memo)
