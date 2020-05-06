class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0 for _ in range(len(nums))]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                memo[i] = num
            elif i == 1:
                memo[i] = max(num, memo[i-1])
            else:
                memo[i] = max(num + memo[i-2], memo[i-1])
        return max(memo[-1], memo[-2])
