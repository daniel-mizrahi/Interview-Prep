class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        results = {}
        ret = 0
        for a in A:
            for b in B:
                if a+b in results:
                    results[a+b] += 1 
                else:
                    results[a+b] = 1     
        for c in C:
            for d in D:
                if (-(c+d)) in results:
                    ret += results[-(c+d)]
        return ret
