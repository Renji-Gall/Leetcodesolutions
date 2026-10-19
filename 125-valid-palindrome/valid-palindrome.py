class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_check = ""
        for i in s:
            if i.isalnum():
                str_check += i.lower()
            rev_str = str_check[::-1]
        
        if rev_str == str_check:
            return True
        return False