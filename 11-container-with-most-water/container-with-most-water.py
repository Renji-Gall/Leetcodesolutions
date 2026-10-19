class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lptr = 0
        rptr = len(height) - 1
        maxarea = 0
        while lptr < rptr:
            maxarea = max(maxarea, min(height[lptr], height[rptr]) * (rptr - lptr))
            if height[lptr] < height[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return maxarea