class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)

        for i in range(length // 2):
            temp = s[i]
            s[i] = s[length - 1]
            s[length - 1] = temp
            length -= 1
        
        return s

