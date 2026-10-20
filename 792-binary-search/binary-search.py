class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            middle =((l+r) // 2)
            if nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            else:
                return middle
        return -1 