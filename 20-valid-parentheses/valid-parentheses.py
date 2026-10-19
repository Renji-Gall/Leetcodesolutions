class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {"}": "{", "]": "[", ")": "("}
        stack = []

        if len(s) % 2 is not 0:
            return False

        for i in s:
            if i in mapping.values():
                stack.append(i)
            if i in mapping.keys():
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if mapping[i] != curr:
                    return False
        return True if len(stack) == 0 else False
