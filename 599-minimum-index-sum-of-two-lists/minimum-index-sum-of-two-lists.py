class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mapping = {}
        leastcommon = []
        minvalue = 1000000
        for i in range(len(list1)):
            mapping[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in mapping:
                currvalue = mapping[list2[i]] + i

                if currvalue < minvalue:
                    minvalue = currvalue
                    leastcommon = [list2[i]]
                elif currvalue == minvalue:
                    leastcommon.append(list2[i])
        return leastcommon
        
    