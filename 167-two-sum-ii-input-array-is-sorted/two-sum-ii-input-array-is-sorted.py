class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr1 = 0
        ptr2 = len(numbers) - 1
        indexes = []
        for i in range(len(numbers)):
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            elif numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            else:
                indexes.append(ptr1 + 1)
                indexes.append(ptr2 + 1)
                return indexes
