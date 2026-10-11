class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        reformated = ""
        grouping = 2 * k
        for i in range(0, len(s), grouping):
            grouped = s[i:i + grouping]
            reverse = grouped[:k][::-1]
            reformated += reverse + grouped[k:]
        return reformated
        