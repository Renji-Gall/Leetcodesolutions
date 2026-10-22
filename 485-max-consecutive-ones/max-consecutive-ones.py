class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxones = 0
        currones = 0
        for i in nums:
            if i == 1:
                currones += 1
            else:
                maxones = max(maxones, currones)
                currones = 0
        maxones = max(maxones, currones)
        return maxones