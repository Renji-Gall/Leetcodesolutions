class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(matrix) - 1
        index = 0
        while l <= r:
            index = ((l + r) // 2)
            if matrix[index][0] <= target:
                l = index + 1
            else:
                r = index - 1
        row = r

        l, r = 0, len(matrix[row]) - 1
        middle = 0
        while l <= r:
            middle = ((l + r) // 2)
            if matrix[row][middle] <= target:
                l = middle + 1
            else:
                r = middle - 1
        return r >= 0 and matrix[row][r] == target       