class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        maxval = 0
        if len(s) == 1:
            return 1

        for i in s:
            if i in longest:
                maxval = max(maxval, len(longest))
                sliceindx = longest.find(i)
                longest = longest[sliceindx+1::] + i
            else:
                longest = longest + i
        maxval = max(len(longest), maxval)
        return maxval