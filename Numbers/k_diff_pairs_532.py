from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ret = 0
        if not k:
            c = Counter(nums)
            for key, value in c.items():
                if value > 1:
                    ret += 1
            return ret
        else:
            if k > 0:
                s = set(nums)
                print(s)
                for num in s:
                    if num - k in s:
                        ret += 1
                return ret
            else:
                return 0
