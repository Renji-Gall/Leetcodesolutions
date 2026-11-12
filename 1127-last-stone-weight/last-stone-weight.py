class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        lengthheap = len(max_heap)
         
        while lengthheap > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            val = x-y
            if val > 0:
                heapq.heappush(max_heap, -val)
            lengthheap = len(max_heap)
        if max_heap:
            return -max_heap.pop()
        else:
            return 0