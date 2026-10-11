class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-", "").upper()

        totallen = len(s)
        remaindergroup = totallen % k
        reformated = ""

        if remaindergroup != 0:
            reformated += s[:remaindergroup] + "-"
        
        for i in range(remaindergroup, totallen, k):
            reformated += s[i:i+k] + "-"

        return reformated[:-1]