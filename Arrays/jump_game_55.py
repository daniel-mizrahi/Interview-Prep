class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        index = 0
        while(index <= furthest and index < (len(nums) - 1)):
            if index != len(nums) - 1:
                furthest = max(furthest, index + nums[index])
            index += 1
        return furthest >= index
