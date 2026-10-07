class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mapping = {}
        mapping2 = {}
        for i in range(len(magazine)):
            if magazine[i] in mapping:
                mapping[magazine[i]] += 1
            else:
                mapping[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in mapping2:
                mapping2[ransomNote[i]] += 1
            else:
                mapping2[ransomNote[i]] = 1
        
        for i in mapping2.keys():
            if i not in mapping:
                return False
            if mapping[i] < mapping2[i]:
                return False
        return True