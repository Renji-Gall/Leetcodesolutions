class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        res = []
        for i in range(len(points)):
    
                value = sqrt((points[i][0] * points[i][0]) + (points[i][1] * points[i][1]))
                arr.append([value, points[i]])

        heapq.heapify(arr)

        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        
        return res