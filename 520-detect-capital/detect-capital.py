class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        case1 = False
        case2 = False
        if word[0] in capital:
            for i in range(1, len(word)):
                if word[i] in lower and case2 is False:
                    case1 = True
                elif word[i] in capital and case1 is False:
                    case2 = True
                else:
                    return False
        else:
            for i in range(1, len(word)):
                if word[i] in capital:
                    return False

        return True
