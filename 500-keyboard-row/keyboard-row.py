class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        currentrow = ""
        test = True
        newstrings = []
        for i in range(len(words)):
            test = True
            if words[i][0].lower() in row1:
                currentrow = row1
            elif words[i][0].lower() in row2:
                currentrow = row2
            else:
                currentrow = row3 
            for x in range(1, len(words[i])):
                if words[i][x].lower() not in currentrow:
                    test = False
                    break
            if test:
                newstrings.append(words[i])
        return newstrings

                
