class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r=s.lower()
        res=""
        for i in r:
            if i.isalnum():
                res+=i
        return res==res[::-1]
        