class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mapping = {}

        for char in s:
            mapping[char] = mapping.get(char, 0) + 1

        for i, char in enumerate(s):
            if mapping[char] == 1:
                return i

        return -1
