import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for val in arr:
            if len(heap) < k:
                heapq.heappush(heap, (-abs(val-x), val))
            else:
                dif1, val_p = heapq.heappop(heap)
                dif2 = -abs(val-x)
                if dif1 == dif2:
                    heapq.heappush(heap, (dif1, min(val_p, val)))
                elif dif1 < dif2:
                    heapq.heappush(heap, (dif2, val))
                else:
                    heapq.heappush(heap, (dif1, val_p))
        return sorted([val for dif, val in heap])
