class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        stack = []
        currstring = ""
    
        for i in range(len(s)):
            if s[i] in alphabet:
                currstring += s[i]
            elif currstring == "":
                continue
            else:
                stack.append(currstring)
                currstring = ""

        if currstring != "":
            stack.append(currstring)

        result = " ".join(stack[::-1])
        return result
