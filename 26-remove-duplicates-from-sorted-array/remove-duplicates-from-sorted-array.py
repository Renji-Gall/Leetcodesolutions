class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums < 1:
            return 0
        
        unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[unique - 1]:
                nums[unique] = nums[i]
                unique += 1
        return unique