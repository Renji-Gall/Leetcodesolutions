class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [-n for n in nums]
        heapq.heapify(arr)

        for i in range(k):
            value = heapq.heappop(arr)
        return -value