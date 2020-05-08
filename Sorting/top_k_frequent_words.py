import collections
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = collections.Counter(words)
        heap = [(value, key) for key, value in dict(frequency).items()]
        # heapq.heapify(heap)
        heap.sort(key= lambda x: (-x[0], x[1]))
        return [val[1] for val in heap[:k]]
