class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapping = {}
        mapping2 = {}

        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]] += 1
            else:
                mapping[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in mapping:
                return t[i]
            if t[i] in mapping2:
                mapping2[t[i]] += 1
                if mapping[t[i]] < mapping2[t[i]]:
                    return t[i]
            if t[i] not in mapping2:
                mapping2[t[i]] = 1