import random
class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        return list(self.original)
        

    def shuffle(self) -> List[int]:
        ret = list(self.original)
        random.shuffle(ret)
        return ret
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
