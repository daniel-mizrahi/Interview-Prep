import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance_to_origin(point):
            return ((point[0])**2 + (point[1])**2)**(0.5)
        heap = []
        for point in points:
            dist = -distance_to_origin(point)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, point))
            else:
                heapq.heappush(heap, (dist, point))
        return [item[1] for item in heap]
